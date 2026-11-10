# Performance Testing Playbook

A short summary of how I approach an engagement.

## 1. Understand
- Business-critical journeys, expected peak volumes, SLAs
- Non-functional requirements from documents and SMEs
- Architecture, environments, data and dependencies

## 2. Plan and estimate
- Test types: baseline, load, stress, spike, soak
- Entry/exit criteria and risks
- Effort in person-hours per sprint, plus tooling and environment cost

## 3. Build
- Parameterised, correlated scripts (JMeter / NeoLoad)
- Realistic data and think times; workload model from production analytics
- Monitoring hooks: APM, infra metrics, logs

## 4. Execute
- Baseline first, then ramp. Change one variable at a time
- Watch for saturation signals, not only averages (p90/p95/p99, errors, throughput)

## 5. Analyse and tune
- Correlate load timeline with traces, CPU/memory/network, DB waits, GC
- Recommend, retest, quantify the delta

## 6. Report and hand over
- Executive summary plus technical appendix
- Capacity guidance and Go-Live baseline
- Automate the regression check in CI/CD
