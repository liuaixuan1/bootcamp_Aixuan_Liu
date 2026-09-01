import pandas as pd


def to_yyyymm(series):
    """
    Convert a datetime Series to YYYYMM integer.
    """
    date = pd.to_datetime(series)

    return (
        date.dt.year * 100
        + date.dt.month
    )


def check_missing(df):
    """
    Return missing-value counts sorted descending.
    """
    return (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )