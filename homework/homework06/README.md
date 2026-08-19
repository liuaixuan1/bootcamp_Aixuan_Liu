# Homework 06 — Data Preprocessing

## Overview

This homework implements a modular data preprocessing workflow using reusable Python functions.

The preprocessing steps include handling missing values, removing columns with excessive missing data, and normalizing numerical variables.

## Cleaning Strategy

### Missing Value Imputation

Missing values in the `age`, `income`, and `score` columns are filled using the median of each column.

Median imputation was selected because it is less sensitive to extreme values than mean imputation.

### Dropping Columns with Excessive Missing Values

Columns with more than 50% missing values are removed.

The `extra_data` column is dropped because most of its observations are missing.

### Normalization

The numerical variables `age`, `income`, and `score` are normalized using min-max scaling.

This transforms each variable to a range between 0 and 1.

The `zipcode` column is treated as an identifier and is not normalized. The `city` column is treated as categorical data.

## Project Structure

```text
homework06/
├── README.md
├── stage06_data-preprocessing_homework-starter.ipynb
├── src/
│   ├── __init__.py
│   └── cleaning.py
└── data/
    ├── raw/
    │   └── sample_data.csv
    └── processed/
        └── sample_data_cleaned.csv