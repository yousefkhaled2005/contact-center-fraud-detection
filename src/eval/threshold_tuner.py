"""
Optimal Decision Threshold Tuner for Asymmetric Telecom Fraud Costs
Copyright (c) 2011-2014 Yousef Khaled.
"""

import numpy as np


class ThresholdOptimizer:
    """
    Minimizes financial loss by balancing false alarms (customer friction) against missed fraud (revenue loss).
    """
    def __init__(self, cost_false_positive: float = 15.0, cost_false_negative: float = 450.0):
        self.c_fp = cost_false_positive
        self.c_fn = cost_false_negative

    def find_optimal_threshold(self, y_true: np.ndarray, y_probs: np.ndarray) -> float:
        thresholds = np.linspace(0.01, 0.99, 100)
        best_thresh = 0.5
        min_loss = float("inf")

        for th in thresholds:
            preds = (y_probs >= th).astype(int)
            fp = np.sum((preds == 1) & (y_true == 0))
            fn = np.sum((preds == 0) & (y_true == 1))
            total_loss = fp * self.c_fp + fn * self.c_fn

            if total_loss < min_loss:
                min_loss = total_loss
                best_thresh = th

        return best_thresh
