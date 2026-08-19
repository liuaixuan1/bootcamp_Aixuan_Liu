import pandas as pd


def fill_missing_median(df, columns):
    """
    Fill missing values in selected numeric columns with
    the median of each column.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    columns : list
        Numeric columns whose missing values should be filled.

    Returns
    -------
    pandas.DataFrame
        Dataframe with missing values filled.
    """
    df = df.copy()

    for column in columns:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)

    return df


def drop_missing(df, threshold=0.5):
    """
    Drop columns whose proportion of missing values
    exceeds the specified threshold.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    threshold : float
        Maximum allowed proportion of missing values.

    Returns
    -------
    pandas.DataFrame
        Dataframe after dropping columns with too many
        missing values.
    """
    df = df.copy()

    missing_ratio = df.isnull().mean()

    columns_to_drop = missing_ratio[
        missing_ratio > threshold
    ].index

    df = df.drop(columns=columns_to_drop)

    return df


def normalize_data(df, columns):
    """
    Normalize selected numeric columns using min-max scaling.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    columns : list
        Numeric columns to normalize.

    Returns
    -------
    pandas.DataFrame
        Dataframe with normalized columns.
    """
    df = df.copy()

    for column in columns:
        min_value = df[column].min()
        max_value = df[column].max()

        if max_value != min_value:
            df[column] = (
                (df[column] - min_value)
                / (max_value - min_value)
            )

    return df