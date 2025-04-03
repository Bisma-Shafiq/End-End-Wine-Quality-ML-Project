from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
from src.mlproject.pipeline.prediction_pipeline import PredictionPipeline
import os

app = Flask(__name__)

# Homepage Route
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

# Training Route (Triggers Model Training)
@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")  # Run your model training script
    return "Training Successfully Done"
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Log received data
        print("Received form data:", request.form)

        # Extract input data
        data = [
            float(request.form["fixed_acidity"]),
            float(request.form["volatile_acidity"]),
            float(request.form["citric_acid"]),
            float(request.form["residual_sugar"]),
            float(request.form["chlorides"]),
            float(request.form["free_sulfur_dioxide"]),
            float(request.form["total_sulfur_dioxide"]),
            float(request.form["density"]),
            float(request.form["ph"]),
            float(request.form["sulphates"]),
            float(request.form["alcohol"])
        ]

        # Load trained model and predict
        model = PredictionPipeline()
        prediction = model.predict(np.array(data).reshape(1, -1))

        return render_template("result.html", prediction=round(prediction[0], 2))

    except Exception as e:
        print("Error:", str(e))  # Log error details
        return render_template("result.html", prediction=f"Error: {str(e)}")

# Result Page Route
@app.route("/result", methods=["GET"])
def result():
    prediction = request.args.get("prediction", None)
    error = request.args.get("error", None)
    return render_template("result.html", prediction=prediction, error=error)

@app.route("/predict_api", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()
        if "features" not in data:
            return jsonify({"error": "Missing 'features' key"}), 400

        features = np.array(data["features"]).reshape(1, -1)
        model = PredictionPipeline()
        prediction = model.predict(features)

        return jsonify({"prediction": round(prediction[0], 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
