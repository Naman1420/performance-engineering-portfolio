#!/usr/bin/env python3
"""Fail the build if a JMeter CSV (.jtl) result breaches thresholds.

Usage:
    python check_thresholds.py results.jtl --p95 2000 --error-rate 1.0

Thresholds apply per transaction label:
    --p95         max 95th percentile elapsed time in ms
    --error-rate  max error percentage
"""
import argparse
import csv
import math
import sys
from collections import defaultdict


def percentile(values, pct):
    values = sorted(values)
    idx = max(0, math.ceil(pct / 100 * len(values)) - 1)
    return values[idx]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("jtl")
    p.add_argument("--p95", type=float, default=2000.0)
    p.add_argument("--error-rate", type=float, default=1.0)
    a = p.parse_args()

    times, errors, counts = defaultdict(list), defaultdict(int), defaultdict(int)
    with open(a.jtl, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            label = row["label"]
            times[label].append(float(row["elapsed"]))
            counts[label] += 1
            if row["success"].strip().lower() != "true":
                errors[label] += 1

    failed = False
    print(f"{'label':30} {'samples':>8} {'p95(ms)':>9} {'err%':>6}  status")
    for label in sorted(times):
        p95 = percentile(times[label], 95)
        err = 100 * errors[label] / counts[label]
        ok = p95 <= a.p95 and err <= a.error_rate
        failed |= not ok
        print(f"{label[:30]:30} {counts[label]:>8} {p95:>9.0f} {err:>6.2f}  {'PASS' if ok else 'FAIL'}")

    print("\nOVERALL:", "FAIL" if failed else "PASS")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
