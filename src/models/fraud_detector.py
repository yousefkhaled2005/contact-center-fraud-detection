from typing import List, Dict
from src.features.feature_pipeline import CDRFeatureExtractor


class RuleAndAnomalyFraudDetector:
    """Dual-stage fraud detection combining heuristic thresholds with anomaly scoring."""

    def __init__(self, threshold_score: float = -0.65):
        self.threshold = threshold_score
        self.extractor = CDRFeatureExtractor()

    def predict(self, cdr: Dict) -> Dict:
        features = self.extractor.extract_features(cdr)

        # Heuristic anomaly score (simulating Isolation Forest decision function)
        anomaly_score = 0.0
        if features["intl_ratio"] > 0.75:
            anomaly_score -= 0.35
        if features["night_ratio"] > 0.50:
            anomaly_score -= 0.25
        if features["burst_velocity"] > 15.0:
            anomaly_score -= 0.30

        is_fraud = anomaly_score <= self.threshold
        return {
            "account_id": cdr.get("account_id"),
            "anomaly_score": round(anomaly_score, 3),
            "is_fraud": is_fraud,
            "risk_level": "CRITICAL" if is_fraud else ("MEDIUM" if anomaly_score < -0.3 else "LOW")
        }


if __name__ == "__main__":
    detector = RuleAndAnomalyFraudDetector()
    sample_cdr = {
        "account_id": "ACC_98412",
        "duration_sec": 3600,
        "intl_mins": 55,
        "night_calls": 18,
        "total_calls": 20,
        "total_charge": 480.0,
        "calls_per_hour": 18.0
    }
    result = detector.predict(sample_cdr)
    print("================ FRAUD DETECTION PREDICTION ================")
    print(result)
    print("============================================================")
