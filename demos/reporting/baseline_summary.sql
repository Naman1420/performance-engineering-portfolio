-- PostgreSQL. Assumed table of raw samples loaded from a JMeter .jtl:
-- CREATE TABLE perf_results (
--   run_id      text,
--   release     text,
--   label       text,
--   elapsed_ms  integer,
--   success     boolean,
--   ts          timestamptz
-- );

-- 1) Per-transaction baseline for a run
SELECT
  run_id,
  label,
  COUNT(*)                                                     AS samples,
  ROUND(AVG(elapsed_ms)::numeric, 0)                           AS avg_ms,
  ROUND((percentile_cont(0.90) WITHIN GROUP (ORDER BY elapsed_ms))::numeric, 0) AS p90_ms,
  ROUND((percentile_cont(0.95) WITHIN GROUP (ORDER BY elapsed_ms))::numeric, 0) AS p95_ms,
  ROUND(100.0 * SUM(CASE WHEN success THEN 0 ELSE 1 END) / COUNT(*), 2)        AS error_pct
FROM perf_results
GROUP BY run_id, label
ORDER BY run_id, label;

-- 2) Baseline vs current release: % change in p95
WITH p95 AS (
  SELECT
    release,
    label,
    percentile_cont(0.95) WITHIN GROUP (ORDER BY elapsed_ms) AS p95_ms
  FROM perf_results
  WHERE release IN ('baseline', 'current')
  GROUP BY release, label
)
SELECT
  b.label,
  ROUND(b.p95_ms::numeric, 0)                                AS baseline_p95_ms,
  ROUND(c.p95_ms::numeric, 0)                                AS current_p95_ms,
  ROUND((100.0 * (c.p95_ms - b.p95_ms) / b.p95_ms)::numeric, 1) AS change_pct
FROM p95 b
JOIN p95 c ON c.label = b.label AND c.release = 'current'
WHERE b.release = 'baseline'
ORDER BY change_pct DESC;
