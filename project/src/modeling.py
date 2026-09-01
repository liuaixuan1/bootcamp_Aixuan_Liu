import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import (
    LinearRegression,
    LassoCV,
    RidgeCV,
    ElasticNetCV
)
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error
)


FEATURES = [
    "PEL1",
    "EPSL1",
    "ROEL1",
    "IPSL1",
    "MTTRL1",
    "BetaL1",
    "M_volL1",
    "M_liqL1",
    "M_highL1",
    "M_skewL1"
]


def time_split(
    data,
    train_ratio=0.7
):

    cut = int(
        len(data)
        * train_ratio
    )

    return (
        data.iloc[:cut],
        data.iloc[cut:]
    )


def make_model(
    model_name="ridge"
):

    if model_name == "ols":

        estimator = (
            LinearRegression()
        )

    elif model_name == "lasso":

        estimator = LassoCV(
            cv=5
        )

    elif model_name == "ridge":

        estimator = RidgeCV(
            alphas=np.logspace(
                -4,
                4,
                50
            )
        )

    elif model_name == "elastic":

        estimator = ElasticNetCV(
            cv=5,
            random_state=42
        )

    else:

        raise ValueError(
            "Unknown model"
        )

    return Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            estimator
        )
    ])


def evaluate_model(
    model,
    test
):

    X = test[FEATURES]

    y = test["M_ExRet"]

    pred = model.predict(X)

    rmse = np.sqrt(
        mean_squared_error(
            y,
            pred
        )
    )

    mae = mean_absolute_error(
        y,
        pred
    )

    return {
        "predictions": pred,
        "rmse": rmse,
        "mae": mae
    }