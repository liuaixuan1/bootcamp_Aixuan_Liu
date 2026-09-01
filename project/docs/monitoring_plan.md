# Monitoring Plan

## Data Layer

### Missing Rate
Metric: monthly missing value rate of each predictor.
Threshold: alert if any key factor > 5%.

### Data Freshness
Metric: days since newest monthly observation.
Threshold: alert if data are > 10 calendar days late.

## Model Layer

### Rolling RMSE
Metric: 12-month rolling RMSE.
Threshold: alert if RMSE increases by > 30% relative to validation baseline.

### Out-of-Sample R²
Metric: rolling OOS R².
Threshold: alert if R² remains below 0 for 6 consecutive months.

## System Layer

### Pipeline Success
Threshold: job success rate < 95%.

### API Latency
Threshold: p95 latency > 1 second.

## Business Layer

### Forecast Usefulness
Monitor whether model-based forecasts outperform historical-mean forecasts.

## Ownership

Analyst reviews factor performance monthly.

Model owner approves retraining.

Technical owner handles pipeline/API failures.