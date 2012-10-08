from src.models.fraud_detector import RuleAndAnomalyFraudDetector
from src.models.churn_predictor import CustomerChurnScorer


def test_fraud_detector():
    detector = RuleAndAnomalyFraudDetector()
    legit_cdr = {"account_id": "1", "duration_sec": 120, "intl_mins": 0, "night_calls": 0, "total_calls": 2, "total_charge": 5, "calls_per_hour": 1}
    assert detector.predict(legit_cdr)["is_fraud"] is False


def test_churn_scorer():
    high_risk = {"customer_id": "C99", "tenure_months": 2, "monthly_charges": 110, "cust_service_calls": 6}
    res = CustomerChurnScorer.calculate_churn_risk(high_risk)
    assert res["retention_flag"] is True
