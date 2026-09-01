from flask import (
    Flask,
    request,
    jsonify
)

import joblib
import pandas as pd


MODEL_PATH = (
    "model/model.pkl"
)

model = joblib.load(
    MODEL_PATH
)

app = Flask(
    __name__
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


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    body = (
        request.get_json(
            silent=True
        )
        or {}
    )

    values = body.get(
        "features"
    )

    if (
        values is None
        or len(values)
        != len(FEATURES)
    ):

        return jsonify({
            "error":
            "10 features required"
        }), 400

    try:

        x = [
            float(v)
            for v in values
        ]

    except (
        ValueError,
        TypeError
    ):

        return jsonify({
            "error":
            "features must be numeric"
        }), 400

    row = pd.DataFrame(
        [x],
        columns=FEATURES
    )

    pred = model.predict(
        row
    )[0]

    return jsonify({
        "predicted_excess_return":
        float(pred)
    })


if __name__ == "__main__":

    app.run(
        port=5000
    )