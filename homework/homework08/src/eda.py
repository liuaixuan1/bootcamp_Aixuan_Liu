import pandas as pd


def eda_summary(df):
    """Return a compact, reusable EDA summary for a pandas DataFrame."""
    rows = []
    n = len(df)

    for col in df.columns:
        s = df[col]

        missing_count = int(s.isna().sum())
        missing_pct = (missing_count / n * 100) if n else 0.0
        nunique = int(s.nunique(dropna=True))

        row = {
            "column": col,
            "dtype": str(s.dtype),
            "missing_count": missing_count,
            "missing_pct": round(missing_pct, 2),
            "n_unique": nunique,
        }

        if pd.api.types.is_numeric_dtype(s):

            non_null = s.dropna()

            row.update({
                "mean": non_null.mean() if len(non_null) else None,
                "std": non_null.std() if len(non_null) else None,
                "min": non_null.min() if len(non_null) else None,
                "max": non_null.max() if len(non_null) else None,
            })

        else:

            counts = s.value_counts(
                dropna=True,
                normalize=True
            )

            row["top_value"] = (
                counts.index[0]
                if len(counts)
                else None
            )

            row["top_share"] = (
                round(float(counts.iloc[0]), 3)
                if len(counts)
                else None
            )

        rows.append(row)

    return pd.DataFrame(rows)