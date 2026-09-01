
from flask import Flask, request, jsonify
import joblib

# Load the model ONCE when the app starts.
# Do not move this inside either route.
model = joblib.load('model/model.pkl')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict_post():
    data = request.get_json(silent=True) or {}

    features = data.get('features')

    # Check that features exists and has exactly 2 values
    if (
        features is None
        or not isinstance(features, list)
        or len(features) != 2
    ):
        return jsonify({
            'error': 'features must be a list containing exactly 2 values'
        }), 400

    # Make sure both values are numeric
    try:
        features = [
            float(features[0]),
            float(features[1])
        ]
    except (TypeError, ValueError):
        return jsonify({
            'error': 'features must contain numeric values'
        }), 400

    prediction = model.predict(
        [features]
    )[0]

    return jsonify({
        'prediction': float(prediction)
    })


@app.route('/predict/<f1>/<f2>', methods=['GET'])
def predict_get(f1, f2):

    try:
        f1 = float(f1)
        f2 = float(f2)

    except ValueError:
        return jsonify({
            'error': 'f1 and f2 must be numeric'
        }), 400

    prediction = model.predict(
        [[f1, f2]]
    )[0]

    return jsonify({
        'prediction': float(prediction)
    })


if __name__ == '__main__':
    app.run(port=5000)
