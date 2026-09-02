# A-share Return Predictability Report

## Executive Summary

This project evaluates whether firm-level financial, trading, liquidity, volatility, and return-distribution characteristics can help predict future excess returns for A-share stock **000635**.

The analysis uses daily and monthly data covering approximately **2001–2023** and constructs ten predictors: PE, EPS, ROE, IPS, MTTR, Beta, M_vol, M_liq, M_high, and M_skew.

The main findings are:

- Some factors show limited predictive information, especially **M_skew**, with weaker evidence for **M_liq** and **M_high**.
- Strong sample-in relationships do not necessarily translate into strong out-of-sample forecasting performance.
- Full multi-factor and regularized models do not consistently outperform simpler specifications.
- Model conclusions are sensitive to factor selection and outlier treatment, so results should be interpreted as research evidence rather than as a production trading signal.
- The most useful next step is to expand the analysis from one stock to a broader A-share universe and evaluate cross-sectional IC and portfolio return spreads.

---

## Research Question

The central research question is:

> Can firm-level financial, trading, liquidity, volatility, and return-distribution factors improve out-of-sample prediction of stock 000635 excess returns relative to a historical-mean benchmark?

The project is designed as a predictive factor-research workflow rather than a causal analysis.

The main decision supported by the analysis is whether the current factor set contains enough stable and economically meaningful predictive information to justify further research and extension to a broader stock universe.

---

## Data

The project uses historical data for stock **000635** from the RESSET database.

The dataset contains both daily and monthly observations.

Daily data are used to construct return-distribution and price-behavior features, while monthly data provide financial, valuation, turnover, risk, and return variables.

The key raw inputs include:

- daily stock returns
- daily closing prices
- monthly trading amount
- monthly turnover rate
- monthly stock return
- monthly risk-free rate
- price-to-earnings ratio
- earnings per share
- return on equity
- operating revenue per share
- monthly beta

The prediction target is monthly excess return:

`M_ExRet = M_r - M_rf`

All predictors are lagged so that information observed at month `t` is used to predict return at month `t+1`.

The data are split chronologically rather than randomly to avoid look-ahead bias.

---

## Factor Construction

The project uses ten predictors.

| Factor | Description |
|---|---|
| PE | Monthly price-to-earnings ratio |
| EPS | Monthly earnings per share |
| ROE | Return on equity |
| IPS | Operating revenue per share |
| MTTR | Monthly turnover rate |
| Beta | Monthly stock beta |
| M_vol | Monthly volatility |
| M_liq | Monthly liquidity measure |
| M_high | Monthly relative price-high measure |
| M_skew | Monthly realized skewness |

Several factors are constructed from daily data.

### M_vol

Monthly volatility is calculated as the sum of squared daily returns within each month.

### M_liq

Monthly liquidity is calculated using monthly return relative to the logarithm of monthly trading amount.

### M_high

The monthly price-high factor compares the current monthly maximum closing price with the maximum price observed over the previous three months.

### M_skew

Monthly realized skewness summarizes asymmetry in the distribution of daily returns.

Each predictor is lagged by one month before modeling so that future information is not used during prediction.

---

## Model Comparison

The project compares several regression approaches:

- Ordinary Least Squares
- LASSO
- Ridge Regression
- ElasticNet

The purpose of this comparison is not simply to identify the model with the best sample-in fit.

Instead, each model is evaluated based on its ability to generalize to unseen future data.

The original experiment showed that model complexity does not automatically improve forecasting quality.

Regularized methods such as LASSO, Ridge, and ElasticNet can help control overfitting and multicollinearity, but their usefulness ultimately depends on out-of-sample performance.

The earlier experiment also found that the predictive ability of individual factors differs substantially.

Among the ten firm-level predictors:

- **M_skew** showed the strongest sample-in statistical evidence.
- **M_liq** and **M_high** showed weaker but still potentially useful evidence.
- Most other factors did not show strong individual significance.

Therefore, both the full-factor model and smaller selected-factor specifications are evaluated.

---

## Out-of-Sample Performance

Out-of-sample evaluation is the main criterion for judging model usefulness.

The project uses a chronological train-test split so that earlier observations are used for model estimation and later observations are reserved for testing.

The main evaluation metrics include:

- RMSE
- MAE
- Out-of-Sample R²
- bootstrap confidence intervals

Out-of-sample R² compares the model against a historical-mean benchmark.

A positive value suggests that the model improves on the benchmark, while a negative value suggests that the model performs worse than simply using the historical average return.

The earlier experiment showed that many model specifications had weak or negative out-of-sample R².

This means that sample-in statistical significance should not be interpreted as sufficient evidence of reliable forecasting ability.

The overall out-of-sample evidence is therefore mixed.

The models may capture limited predictive structure, but the signal is not strong or stable enough to support a high-confidence forecasting claim.

---

## Sensitivity Analysis

Three main scenarios are compared.

### Scenario 1 — Baseline

The baseline model uses all ten lagged predictors.

This represents the full multi-factor specification.

### Scenario 2 — Selected Factors

This scenario uses only:

- M_liq
- M_high
- M_skew

These factors were selected because they showed the strongest statistical evidence in the earlier analysis.

The purpose is to test whether a smaller and more interpretable model can reduce noise and improve out-of-sample stability.

### Scenario 3 — Winsorized Predictors

This scenario keeps all ten factors but limits extreme predictor values.

Winsorization thresholds are estimated only from the training sample to avoid data leakage.

The purpose is to evaluate whether model performance is sensitive to extreme observations.

### Sensitivity Takeaway

If all three scenarios produce similar RMSE, MAE, and out-of-sample R², the model conclusion is relatively robust.

If performance changes materially across scenarios, the result depends strongly on modeling assumptions.

Bootstrap confidence intervals are also used to show that prediction error should be interpreted as a range rather than as a precise single number.

Overall, the scenario analysis suggests that model conclusions should be viewed as conditional on factor selection and data treatment choices.

---

## Assumptions & Risks

### Time-Stability Assumption

The models assume that historical relationships between predictors and future returns remain sufficiently stable through time.

This may fail during structural market changes or different market regimes.

### Single-Stock Limitation

The project studies only stock 000635.

Results from one stock cannot be generalized directly to the full A-share market.

### Look-Ahead Risk

Financial prediction is highly sensitive to timing errors.

All features must be constructed using information available before the predicted return period.

### Outlier Sensitivity

Extreme observations may have a large effect on regression coefficients and prediction errors.

This risk is addressed through a winsorized scenario, but different outlier definitions may produce different results.

### Overfitting Risk

Testing many predictors and models increases the risk of identifying apparent relationships that exist only in the historical sample.

Out-of-sample evaluation is therefore more important than sample-in fit.

### Data Quality Risk

The analysis depends on correct date alignment, missing-value treatment, and consistency between daily and monthly datasets.

Errors in preprocessing could materially affect the final results.

### Economic Significance Risk

Statistical significance does not automatically imply that the signal would remain useful after transaction costs, turnover, liquidity constraints, and implementation costs.

---

## Decision Implications

The current factor set should be treated as a **research candidate**, not as a production trading signal.

The evidence suggests that a small subset of factors may contain useful predictive information, particularly M_skew and potentially M_liq and M_high.

However, the weak and unstable out-of-sample performance means that the current model does not provide sufficiently strong evidence for immediate investment implementation.

For a quantitative portfolio manager, the practical implications are:

- do not rely on sample-in significance alone;
- prioritize out-of-sample performance;
- prefer simpler models when predictive performance is similar;
- evaluate factor stability across different market regimes;
- test results across a broader stock universe before committing research or portfolio capital;
- monitor model degradation if the model is reused over time.

The correct decision at this stage is to continue research rather than deploy the model directly.

---

## Next Steps

The next stage of research should focus on external validity and broader cross-sectional testing.

Recommended extensions include:

1. Expand the stock universe from one stock to a large sample of A-share securities.
2. Construct the same factors consistently for every stock.
3. Calculate monthly cross-sectional Information Coefficients.
4. Evaluate IC significance and IC stability through time.
5. Sort stocks into factor quantiles and calculate top-minus-bottom portfolio return spreads.
6. Control for industry, size, value, and market exposures.
7. Include transaction costs and turnover constraints.
8. Test performance separately across bull, bear, and high-volatility market regimes.
9. Use expanding-window or rolling-window validation.
10. Compare traditional predictors with alternative signals such as short-term news sentiment.

A particularly valuable extension would be to add a stock-level news-sentiment factor and test whether it provides incremental predictive power beyond the existing financial and trading variables.

The ultimate goal is to determine whether the signal remains statistically meaningful, economically relevant, and robust enough to justify inclusion in a broader multi-factor research framework.