# A-share Stock Return Predictability Research

**Lifecycle:** End-to-End Financial Data Science Project

## Problem Statement

A quantitative investment research team wants to determine whether firm-level financial, trading, and price-distribution characteristics contain predictive information for future A-share stock returns.

This project studies stock 000635 using daily and monthly data from 2001–2023. The analysis evaluates whether individual predictors and multi-factor models provide statistically and economically meaningful out-of-sample return forecasts.

## Stakeholder & User

The primary decision-maker is a quantitative portfolio manager.

Quantitative research analysts will use the project outputs to:

- identify potentially useful predictive factors;
- compare traditional linear models with regularized machine-learning models;
- understand model uncertainty and failure risks;
- determine whether the factor set deserves further research.

## Core Research Question

Do firm-level financial and trading factors improve out-of-sample prediction of stock 000635 returns relative to a historical-mean benchmark?

## Core Factors

- PE
- EPS
- ROE
- IPS
- MTTR
- Beta
- M_vol
- M_liq
- M_high
- M_skew

## Target

Monthly excess return:

`M_ExRet = M_r - M_rf`

## Core Evaluation Metrics

- coefficient significance and p-values
- out-of-sample R²
- MSFE-adjusted statistic
- RMSE / MAE
- economic utility improvement ΔU

## Assumptions & Risks

- Predictors at month t must only predict return at t+1.
- Time ordering must be preserved.
- Missing values and extreme observations may affect results.
- Relationships may change across market regimes.
- Results from one stock cannot automatically generalize to the full A-share universe.

## Goal → Lifecycle → Deliverable

| Goal | Lifecycle Stage | Deliverable |
|---|---|---|
| Define research question | Problem Framing | README |
| Build reproducible environment | Tooling | repo structure |
| Acquire raw data | Acquisition | data/raw |
| Clean and align data | Preprocessing | data/processed |
| Construct predictors | Feature Engineering | src/features.py |
| Test predictive models | Modeling | modeling notebook |
| Quantify model risk | Evaluation | evaluation report |
| Communicate findings | Delivery | final report |
| Package workflow | Productization | Flask API |
| Design monitoring | Deployment | monitoring plan |
| Define pipeline | Orchestration | orchestration plan |
| Review lifecycle | Lifecycle Review | final summary |

## Data Storage

Raw RESSET files are stored in `data/raw/`.

Cleaned factor-ready data are stored in:

`data/processed/factor_data.csv`

The project reads paths through `src/config.py` so that notebooks do not contain machine-specific absolute paths.

Because raw RESSET data may be subject to licensing restrictions, raw `.xls` files should not be uploaded to a public GitHub repository unless redistribution is permitted.