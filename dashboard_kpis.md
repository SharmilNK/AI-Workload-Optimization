# Dashboard KPIs

- model_usage_pct_by_type
- cost_usd_total (per day)
- avg_quality_by_model
- routing_efficiency_pct (requests not sent to large model)
- error_rate and retries
- baseline_cost_vs_optimized_cost

Alert thresholds:
- cost spike: cost in last hour > 2x hourly avg
- quality drop: avg quality last 24h < 3.5
