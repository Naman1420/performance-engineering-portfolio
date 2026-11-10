# CI/CD performance gate demo

- `check_thresholds.py`: reads a JMeter `.jtl` CSV, computes p95 and error rate per transaction, exits non-zero on breach (stdlib only).
- `Jenkinsfile`: runs JMeter headless, then the gate, then archives results.
- `azure-pipelines.yml`: same flow for Azure DevOps.

Thresholds should come from your baseline (see [`demos/reporting`](../reporting/)).
