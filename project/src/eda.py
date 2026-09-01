def eda_summary(df):

    return {
        "shape": df.shape,
        "missing": df.isna().sum(),
        "describe": df.describe().T
    }