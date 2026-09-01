import numpy as np
import pandas as pd


FACTOR_COLUMNS = [
    "PE",
    "EPS",
    "ROE",
    "IPS",
    "MTTR",
    "Beta",
    "M_vol",
    "M_liq",
    "M_high",
    "M_skew"
]


def build_features(
    daily,
    monthly
):

    data = monthly.copy()

    # Excess return
    data["M_ExRet"] = (
        data["M_r"]
        - data["M_rf"]
    )

    # Monthly volatility
    m_vol = (
        daily
        .groupby("yyyymm")["day_r"]
        .apply(
            lambda x:
            (x ** 2).sum()
        )
        .rename("M_vol")
    )

    data = data.merge(
        m_vol,
        left_on="yyyymm",
        right_index=True,
        how="left"
    )

    # Liquidity
    data["M_liq"] = (
        data["M_r"]
        /
        np.log(data["Amount"])
    )

    # Monthly high
    monthly_high = (
        daily
        .groupby("yyyymm")["close"]
        .max()
        .rename("month_high")
        .to_frame()
    )

    previous_3m_high = (
        monthly_high["month_high"]
        .shift(1)
        .rolling(
            3,
            min_periods=1
        )
        .max()
    )

    monthly_high["M_high"] = (
        monthly_high["month_high"]
        /
        previous_3m_high
    )

    data = data.merge(
        monthly_high[["M_high"]],
        left_on="yyyymm",
        right_index=True,
        how="left"
    )

    # Realized skewness
    grouped = daily.groupby("yyyymm")

    n = grouped["day_r"].count()

    sum_cube = grouped["day_r"].apply(
        lambda x: (x ** 3).sum()
    )

    skew = (
        np.sqrt(n)
        * sum_cube
        /
        data.set_index("yyyymm")[
            "M_vol"
        ] ** 1.5
    )

    skew.name = "M_skew"

    data = data.merge(
        skew,
        left_on="yyyymm",
        right_index=True,
        how="left"
    )

    # Lag predictors: t information predicts t+1
    for factor in FACTOR_COLUMNS:

        data[
            f"{factor}L1"
        ] = data[factor].shift(1)

    return (
        data
        .sort_values("yyyymm")
        .dropna()
        .reset_index(drop=True)
    )