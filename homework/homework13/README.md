# Stage 13 Homework - Prediction API

This project serves a linear regression model through a Flask API.
The model takes two numeric features as input and returns a continuous numerical prediction.

## Running the API

From the `homework/homework13` directory, run:

```bash
python app.py
```

The server runs at `http://127.0.0.1:5000`.

The trained model is loaded once from `model/model.pkl` when the Flask application starts.

## POST /predict

The POST route accepts a JSON body containing exactly two numeric features.

Example request:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [0.1, 0.2]}"
```

Example response:

```json
{"prediction":23.58961171297328}
```

## GET /predict/<f1>/<f2>

The GET route accepts the two numeric features directly in the URL.

Example request:

```bash
curl http://127.0.0.1:5000/predict/0.1/0.2
```

Example response:

```json
{"prediction":23.58961171297328}
```

## Bad Input

Invalid input returns HTTP status code `400` and a JSON error message instead of a traceback.

Example invalid request:

```bash
curl http://127.0.0.1:5000/predict/abc/0.2
```

Example response:

```json
{"error":"f1 and f2 must be numeric"}
```

The POST route also returns HTTP `400` when:

- the `features` key is missing;
- the `features` list does not contain exactly two values;
- either feature is not numeric.