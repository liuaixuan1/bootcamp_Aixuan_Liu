# Stakeholder Memo: Short‑term News Sentiment Factor Research
Date: Homework Stage 01
Audience: Quant Portfolio Manager & Quant Research Analysts

## TL;DR
This research project evaluates whether pre‑computed short‑term news sentiment signals bring additional predictive value for A‑share stock future returns. We will produce factor performance metrics and robustness checks to help decide if this factor should enter our multi‑factor candidate pool. This memo covers project scope, expected outputs, key assumptions, risks and follow‑up work.

## Business Context
Our existing multi‑factor model mainly relies on financial indicators and price‑volume features. We want to explore alternative data sources such as news sentiment to capture market investor mood. Currently we lack systematic validation: it is unknown whether sentiment can provide incremental alpha beyond our existing factor set. Before spending more engineering resources, we need offline analysis to test signal quality.

## What the analysis will deliver
‑ Clean aligned dataset combining daily stock returns and news sentiment scores.
‑ Factor evaluation notebook calculating IC, p‑value and quantile stratified return spread.
‑ Robustness test results across different market periods.
‑ Summary report judging whether the sentiment factor has meaningful predictive capability.

## Important limitations & assumptions
1. We use off‑the‑shelf pre‑calculated sentiment scores. This project will not build custom natural‑language models for news parsing.
2. All analysis is offline back‑test research. Positive back‑test performance does not guarantee real‑trading profitability.
3. Strict time‑based split is required to prevent look‑ahead bias, which is a major risk in factor research.
4. Copyright‑restricted raw news text will not be stored in the public code repository.

## Risks to watch
‑ Market regime risk: sentiment factor may work well in some market environments and fail in others. We test performance in sub‑periods to observe stability.
‑ Signal noise risk: low‑quality news sentiment labels may produce false signals. We will filter low‑confidence records for robustness comparison.
‑ Overfitting risk: repeated tweaking parameters to chase good in‑sample results. Final judgement is fully based on out‑of‑sample performance.

## Next Steps
1. Finish problem framing and GitHub repository setup (Stage 01 deliverable).
2. Later stages: data loading, cleaning, handling missing values and exploratory analysis.
3. Compute sentiment factor and run standard factor evaluation workflow.
4. Summarize performance and draw conclusions on factor research value.

## Where to find project material
All notebooks, source code and documentation are stored within the course shared GitHub repository.
