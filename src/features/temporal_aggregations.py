"""
Temporal Sliding Window Feature Engineering on CDR Call Streams
Copyright (c) 2011-2014 Yousef Khaled.
"""

import pandas as pd
import numpy as np


class CDRTemporalAggregator:
    """
    Computes rolling velocity metrics to detect rapid SIM box bursts and robocall campaigns.
    """
    def __init__(self, windows=("1h", "6h", "24h")):
        self.windows = windows

    def compute_call_velocity(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.sort_values("timestamp").copy()
        df["call_count_1"] = 1
        grouped = df.set_index("timestamp").groupby("caller_msisdn")
        
        features = pd.DataFrame(index=df.index)
        features["calls_last_1h"] = grouped["call_count_1"].rolling("1h").count().values
        features["duration_sum_1h"] = grouped["duration_sec"].rolling("1h").sum().values
        features["unique_callees_1h"] = grouped["callee_msisdn"].rolling("1h").apply(lambda s: len(set(s)), raw=False).values
        return features
