from typing import List, Dict
import math


class CDRFeatureExtractor:
    """Extracts statistical anomaly features from raw Call Detail Records (CDRs)."""

    @staticmethod
    def extract_features(cdr: Dict) -> Dict[str, float]:
        duration = float(cdr.get("duration_sec", 0))
        intl_mins = float(cdr.get("intl_mins", 0))
        night_calls = float(cdr.get("night_calls", 0))
        total_charge = float(cdr.get("total_charge", 0))

        # Ratios indicative of SIM box and PBX hacking fraud
        intl_ratio = intl_mins / max((duration / 60.0), 1.0)
        night_ratio = night_calls / max(float(cdr.get("total_calls", 1)), 1.0)
        cost_per_min = total_charge / max((duration / 60.0), 0.1)

        return {
            "duration_sec": duration,
            "intl_ratio": round(intl_ratio, 3),
            "night_ratio": round(night_ratio, 3),
            "cost_per_min": round(cost_per_min, 3),
            "burst_velocity": round(float(cdr.get("calls_per_hour", 1)), 2)
        }
