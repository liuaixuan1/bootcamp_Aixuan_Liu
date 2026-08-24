import pandas as pd


def add_features(df):
    """
    Add engineered features for the
    Short-term Sentiment Factor Research Project.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw stock-day dataframe.

    Returns
    -------
    pandas.DataFrame
        Dataframe with engineered features.
    """

    df = df.copy()

    # Sort before creating time-series features
    df = df.sort_values(
        ["stock_id", "date"]
    ).reset_index(drop=True)

    # --------------------------------------------------
    # Feature 1:
    # Confidence-weighted sentiment
    # --------------------------------------------------

    df["confidence_weighted_sentiment"] = (
        df["news_sentiment"]
        * df["sentiment_confidence"]
    )

    # --------------------------------------------------
    # Feature 2:
    # 3-day sentiment change
    # --------------------------------------------------

    df["sentiment_lag_3d"] = (
        df
        .groupby("stock_id")["news_sentiment"]
        .shift(3)
    )

    df["sentiment_change_3d"] = (
        df["news_sentiment"]
        - df["sentiment_lag_3d"]
    )

    # --------------------------------------------------
    # Feature 3:
    # Market regime categorical encoding
    # --------------------------------------------------

    regime_dummies = pd.get_dummies(
        df["market_regime"],
        prefix="regime",
        dtype=int
    )

    df = pd.concat(
        [
            df,
            regime_dummies
        ],
        axis=1
    )

    return df