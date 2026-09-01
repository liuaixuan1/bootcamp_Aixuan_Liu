# Lifecycle Framework Guide

| Stage | Project Artifact | Key Decision |
|---|---|---|
| 01 Problem Framing | README.md | Test stock-return predictability |
| 02 Tooling | requirements.txt / config.py | Reproducible project structure |
| 03 Python Fundamentals | utils.py | Modular helper functions |
| 04 Acquisition | data/raw / ingestion.py | RESSET input layer |
| 05 Storage | data/raw / processed | Separate raw and derived data |
| 06 Preprocessing | cleaning.py | Clean and align monthly/daily data |
| 07 Outliers | outliers.py | Explicit extreme-value treatment |
| 08 EDA | eda.ipynb / eda.py | Understand factor distributions |
| 09 Features | features.py | Construct 10 predictive factors |
| 10 Modeling | modeling.py / modeling.ipynb | OLS and regularized regression |
| 11 Evaluation | evaluation.py | OOS performance and sensitivity |
| 12 Delivery | reports/final_report.md | Stakeholder-facing results |
| 13 Productization | app.py / model.pkl | Reusable prediction API |
| 14 Monitoring | monitoring_plan.md | Define production risks |
| 15 Orchestration | run_step.py | Reproducible pipeline execution |
| 16 Lifecycle Review | project_summary.md | Final project documentation |