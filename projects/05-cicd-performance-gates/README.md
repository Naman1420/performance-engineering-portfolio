# 5. CI/CD Performance Gates

**Role:** Performance Test Engineer (commercial project) · **Tools:** Jenkins, Azure DevOps, JMeter

## Problem
Performance regressions were found late, after functional testing, when they were costly to fix.

## What I did
Integrated automated performance test execution into **Jenkins and Azure DevOps** pipelines so performance regression testing runs at every deployment stage, with pass/fail thresholds.

## Demo
[`demos/cicd`](../../demos/cicd/) has a Jenkinsfile and a threshold-gate script for JMeter results.
