import pandas as pd


def clean_daily_data(df):

    out = df.copy()

    out["date"] = pd.to_datetime(
        out["date"]
    )

    out["yyyymm"] = (
        out["date"].dt.year * 100
        + out["date"].dt.month
    )

    out["close"] = pd.to_numeric(
        out["close"],
        errors="coerce"
    )

    out["day_r"] = pd.to_numeric(
        out["day_r"],
        errors="coerce"
    )

    out = (
        out
        .dropna(
            subset=[
                "yyyymm",
                "close",
                "day_r"
            ]
        )
        .sort_values("date")
        .reset_index(drop=True)
    )

    return out


def clean_monthly_data(
    monthly,
    beta
):

    m = monthly.copy()
    b = beta.copy()

    m["date"] = pd.to_datetime(
        m["date"]
    )

    b["date"] = pd.to_datetime(
        b["date"]
    )

    m["yyyymm"] = (
        m["date"].dt.year * 100
        + m["date"].dt.month
    )

    b["yyyymm"] = (
        b["date"].dt.year * 100
        + b["date"].dt.month
    )

    m = m.drop(
        columns=["date"]
    )

    b = b.drop(
        columns=["date"]
    )

    out = pd.merge(
        m,
        b,
        on="yyyymm",
        how="inner"
    )

    out = (
        out
        .sort_values("yyyymm")
        .drop_duplicates("yyyymm")
        .reset_index(drop=True)
    )

    return out