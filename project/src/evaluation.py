import numpy as np


def r2_oos(
    y_true,
    y_pred,
    benchmark
):

    denominator = np.sum(
        (y_true - benchmark) ** 2
    )

    numerator = np.sum(
        (y_true - y_pred) ** 2
    )

    return (
        1
        - numerator / denominator
    )


def bootstrap_rmse(
    y_true,
    y_pred,
    n_boot=1000,
    seed=42
):

    rng = np.random.default_rng(
        seed
    )

    values = []

    n = len(y_true)

    for _ in range(n_boot):

        idx = rng.choice(
            n,
            n,
            replace=True
        )

        rmse = np.sqrt(
            np.mean(
                (
                    y_true[idx]
                    - y_pred[idx]
                ) ** 2
            )
        )

        values.append(
            rmse
        )

    values = np.array(
        values
    )

    return {
        "mean": values.mean(),
        "lower": np.percentile(
            values,
            2.5
        ),
        "upper": np.percentile(
            values,
            97.5
        )
    }