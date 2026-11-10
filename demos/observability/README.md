# Observability demo: JMeter -> InfluxDB -> Grafana

## Run
```bash
docker compose up -d
```
Grafana: http://localhost:3000 (default login `admin` / `admin`, change on first login).

## Connect JMeter
Add a **Backend Listener** to your test plan:

| Setting | Value |
|---|---|
| Backend Listener implementation | `org.apache.jmeter.visualizers.backend.influxdb.InfluxdbBackendListenerClient` |
| influxdbUrl | `http://localhost:8086/write?db=jmeter` |
| application | `demo-app` |
| measurement | `jmeter` |
| summaryOnly | `false` |
| testTitle | `baseline-run-01` |

## Dashboards
Import a community JMeter dashboard in Grafana, or build panels for:
- Throughput (requests/sec)
- p90 / p95 response time per transaction
- Error rate
- Active threads

Tag runs with `testTitle` so you can compare releases side by side.
