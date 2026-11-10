# 2. Cloud & Container Monitoring and Root Cause Analysis

**Role:** Performance Test Engineer · **Tools:** DataDog, Dynatrace, Azure App Insights, Kubernetes, AppDynamics, Splunk

## Problem
Slowdowns in Kubernetes-orchestrated environments are hard to attribute: is it the application, the container limits, the database or the network?

## What I did
- Monitored CPU, memory and network utilisation of workloads running in Kubernetes using DataDog, Dynatrace and Azure App Insights.
- Correlated load-test timelines with APM traces, logs and infrastructure metrics to isolate bottlenecks.
- Ran deep-dive diagnostics on production-level performance issues and recommended application configuration tuning.

## Results
- **20%+ improvement in system efficiency** from resource-utilisation findings
- **25% reduction in response times** from configuration tuning recommendations

## Typical RCA workflow
1. Reproduce under controlled load and capture the baseline
2. Find the slowest transactions and drill into traces
3. Check saturation: CPU throttling, memory pressure, connection pools, GC, DB waits
4. Form a hypothesis, change one variable, retest
5. Document the finding, the fix and the measured delta
