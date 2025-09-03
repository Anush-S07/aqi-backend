from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = "best_aqi_model.pkl"
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
        print("Model loaded successfully.")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Please deploy with best_aqi_model.pkl"}), 500
    try:
        # Parse input from JSON
        data = request.get_json()

        pm25 = float(data["pm25"])
        pm10 = float(data["pm10"])
        co = float(data["co"]) / 1000
        so2 = float(data["so2"])
        no2 = float(data["no2"])
        o3 = float(data["o3"])

        input_data = np.array([[pm25, pm10, co, so2, no2, o3]])
        prediction = model.predict(input_data)
        aqi_value = prediction[0]

        if aqi_value <= 50:
            category, color, description = "Good", "green", "Minimal or no impact on health"
        elif aqi_value <= 100:
            category, color, description = "Moderate", "yellow", "Breathing discomfort for sensitive groups"
        elif aqi_value <= 150:
            category, color, description = "Unhealthy for Sensitive Groups", "orange", "Health effects for sensitive individuals"
        elif aqi_value <= 200:
            category, color, description = "Unhealthy", "lightred", "Health effects on the general population"
        elif aqi_value <= 300:
            category, color, description = "Very Unhealthy", "lightpurple", "Serious health effects"
        else:
            category, color, description = "Hazardous", "maroon", "Severe health effects; emergency conditions"

        return jsonify({
            "aqi": round(aqi_value, 2),
            "category": category,
            "description": description,
            "color": color,
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
