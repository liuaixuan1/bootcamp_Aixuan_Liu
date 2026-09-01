def flag_iqr_outliers(
    df,
    column,
    k=1.5
):

    out = df.copy()

    q1 = out[column].quantile(0.25)

    q3 = out[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    out[
        f"{column}_outlier"
    ] = (
        (out[column] < lower)
        |
        (out[column] > upper)
    )

    return out