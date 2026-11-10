# Reporting demo

`baseline_summary.sql` shows two patterns used for Go-Live baselines:

1. Per-transaction avg / p90 / p95 / error rate.
2. Baseline-vs-current comparison, flagging regressions by % change in p95.

**DAX tips for faster report generation**
- Prefer measures over calculated columns; avoid row-by-row iterators when an aggregation works.
- Use `VAR` to avoid recomputing the same expression.
- Pre-aggregate in SQL and keep the model narrow before importing into PowerBI.
