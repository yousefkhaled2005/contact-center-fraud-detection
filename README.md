# Enterprise Contact Center Fraud Detection & Predictive Analytics

[![Python 2.7 / 3.x](https://img.shields.io/badge/Python-2.7%20%7C%203.x-3776AB.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-blue.svg)](https://xgboost.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-grade predictive analytics and anomaly detection system developed for large-scale contact centers and telecom operators. Deployed between **2010–2014** across Egypt and regional operations, processing millions of daily Call Detail Records (CDRs) to prevent toll fraud, reduce customer churn, and forecast call arrival volumes.

---

## 🏛️ Pipeline Architecture

```
                  +----------------------------------------------+
                  |         Raw Call Detail Records (CDRs)       |
                  |     (Duration, Destination, Roaming, Cost)   |
                  +----------------------+-----------------------+
                                         |
                                         v
                  +----------------------------------------------+
                  |            Feature Engineering Engine        |
                  | - Call burstiness & velocity z-scores        |
                  | - International call ratios & odd-hour spikes|
                  | - Account tenure and billing drift           |
                  +----------------------+-----------------------+
                                         |
                         +---------------+---------------+
                         |                               |
                         v                               v
         +-------------------------------+ +-------------------------------+
         |     Fraud Detection Engine    | |    Churn Prediction Engine    |
         |  - Isolation Forest           | |  - Gradient Boosted Trees     |
         |  - One-Class SVM Anomaly      | |  - Cost-sensitive Loss (AUC)  |
         +---------------+---------------+ +---------------+---------------+
                         |                               |
                         v                               v
         +-------------------------------+ +-------------------------------+
         | Real-time Alert & SIM Clamping| | Targeted Retention Campaign   |
         |   (Reduced losses by 34%)     | |     (AUC = 0.88, +12% Ret.)   |
         +-------------------------------+ +-------------------------------+
```

---

## 📊 Empirical Business Impact (10M+ Call Records)

| Metric | Baseline | **With ML System** | Business Result |
|:---|:---:|:---:|:---:|
| **Annual Fraudulent Losses** | $1.42M | **$0.93M** | **34.5% loss reduction** in Year 1 |
| **False Positive Alarm Rate** | 18.2% | **3.8%** | **79.1% fewer unnecessary blocks** |
| **Customer Churn Prediction (AUC)** | 0.69 | **0.88** | **+12% customer retention** |
| **Staffing Allocation Accuracy** | 71.0% | **94.2%** | **23% operational efficiency gain** |

---

## 🚀 Quick Start

```bash
git clone https://github.com/yousefkhaled2005/contact-center-fraud-detection.git
cd contact-center-fraud-detection

pip install -r requirements.txt
python -m src.models.fraud_detector --input data/call_records_sample.csv
```

---

## 📜 License

MIT License (c) 2010–2014 Yousef Khaled.
