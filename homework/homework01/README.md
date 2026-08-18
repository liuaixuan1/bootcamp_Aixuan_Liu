# Short‑term Sentiment Factor Research Project

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
A small quantitative investment team wants to explore whether short‑term news sentiment signals can improve A‑share stock return forecasts. Currently the team only uses traditional financial and price‑volume features. It is unclear whether news‑derived sentiment contains incremental predictive power that cannot be captured by existing factors. Manual screening of news text is inefficient and cannot quantify sentiment‑return relationships systematically. This project will build an analytical workflow to test the effectiveness of sentiment‑based stock factors. The core decision is whether to add this new factor into the multi‑factor research pool for further back‑test. Success will be measured by out‑of‑sample factor IC (Information Coefficient) and group return spread.

## Stakeholder & User
The decision‑maker is the quantitative portfolio manager, who decides whether to allocate research resources to this new factor and whether to include it in factor combination experiments. End‑users are quantitative research analysts, who will use analysis outputs to evaluate factor quality and compare it against existing risk factors. Analysis results are expected before monthly factor review meetings and should integrate with existing factor‑research notebook pipelines.

## Useful Answer & Decision
This is a **predictive** analysis task.
‑ Core metrics: out‑of‑sample IC value, IC p‑value, quantile group return spread.
‑ Deliverable artifact: data processing script, factor evaluation notebook, summary report documenting factor performance and robustness checks.
The output supports the decision: whether the news‑sentiment factor shows statistically meaningful predictive power for future stock returns and deserves further research investment.

## Assumptions & Constraints
‑ Daily news sentiment score dataset covering target A‑share stocks is available for research.
‑ Only offline research work; no real‑time factor calculation module or live trading system will be built.
‑ Limited computing resources; heavy deep‑learning sentiment retraining is out‑of‑scope. We use provided pre‑computed sentiment scores.
‑ Analysis must follow standard factor research rules: strictly time‑series train‑test split to avoid look‑ahead bias.
‑ Raw news text with copyright restrictions cannot be uploaded to the public GitHub repository.

## Known Unknowns / Risks
‑ Sentiment factor performance may decay under different market regimes (bull / bear / volatile market); will test factor performance across different market periods.
‑ Noise inside news sentiment labeling may weaken factor signal strength; will conduct robustness tests by filtering low‑confidence sentiment entries.
‑ Factor over‑fitting risk from repeated parameter tuning; final evaluation must rely purely on unseen out‑of‑sample data.

## Lifecycle Mapping
Goal → Stage → Deliverable
‑ Define factor‑research problem and project boundaries → Problem Framing & Scoping (Stage 01) → Project README + stakeholder memo artifact

## Repo Plan
Folders: `data/`, `src/`, `notebooks/`, `docs/`
‑ `data/raw`: original sentiment and stock return input datasets
‑ `data/processed`: aligned, cleaned factor‑ready datasets
‑ `src`: reusable functions for factor calculation, IC computation, quantile back‑test
‑ `notebooks`: exploratory data analysis, factor performance evaluation notebooks
‑ `docs`: stakeholder memo, project notes
Update cadence: create git commits upon completion of each homework stage.
