# Dashboard KPIs

- model_usage_pct_by_type
Model usage %
Shows how often each model is used
Proves routing is working (or not)

- cost_usd_total (per day)
Total cost
Shows real business impact
This is what finance cares about

- avg_quality_by_model
Average quality score
Prevents “cheap but useless” AI
Balances cost vs correctness

- routing_efficiency_pct (requests not sent to large model)
Routing efficiency
% of requests NOT sent to large model
Direct signal of optimization success

- error_rate and retries
Error rate
Shows reliability
High error = bad prompts, wrong routing, or model mismatch

- baseline_cost_vs_optimized_cost

Alert thresholds:
- cost spike: cost in last hour > 2x hourly avg
- quality drop: avg quality last 24h < 3.5
