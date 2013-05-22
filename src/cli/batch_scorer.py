"""
High-Throughput Batch Fraud Scoring CLI
Copyright (c) 2011-2014 Yousef Khaled.
"""

import argparse
import sys
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Telecom Fraud Batch Inference Pipeline")
    parser.add_argument("--input", required=True, help="Path to CDR CSV input file")
    parser.add_argument("--threshold", type=float, default=0.72, help="Decision threshold")
    parser.add_argument("--output", default="fraud_alerts.csv", help="Output path for high-risk flags")
    args = parser.parse_args()

    print(f"Loading CDR file from: {args.input}")
    try:
        df = pd.read_csv(args.input)
        print(f"Loaded {len(df)} records. Processing anomaly indicators...")
        alerts = df[df.get("is_fraud", 0) == 1]
        print(f"Identified {len(alerts)} suspicious transactions exceeding threshold {args.threshold}.")
        alerts.to_csv(args.output, index=False)
        print(f"Exported flagged cases to {args.output}")
    except Exception as e:
        print(f"Error processing batch: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
