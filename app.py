from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Accept JSON or Form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Extract values
        pm25 = float(data.get("pm25", 0))
        pm10 = float(data.get("pm10", 0))
        co = float(data.get("co", 0)) / 1000  # convert ppb to ppm if needed
        so2 = float(data.get("so2", 0))
        no2 = float(data.get("no2", 0))
        o3 = float(data.get("o3", 0))

        # Prepare input for model
        input_data = np.array([[pm25, pm10, co, so2, no2, o3]])

        # Predict AQI
        prediction = model.predict(input_data)
        aqi_value = prediction[0]

        # Categorize AQI
        if aqi_value <= 50:
            category = "Good"
            color = "green"
            description = "Minimal or no impact on health"
        elif aqi_value <= 100:
            category = "Moderate"
            color = "yellow"
            description = "Breathing discomfort for sensitive groups"
        elif aqi_value <= 150:
            category = "Unhealthy for Sensitive Groups"
            color = "orange"
            description = "Health effects for sensitive individuals"
        elif aqi_value <= 200:
            category = "Unhealthy"
            color = "red"
            description = "Health effects on the general population"
        elif aqi_value <= 300:
            category = "Very Unhealthy"
            color = "purple"
            description = "Serious health effects"
        else:
            category = "Hazardous"
            color = "maroon"
            description = "Severe health effects; emergency conditions"

        return jsonify({
            "aqi": round(aqi_value, 2),
            "category": category,
            "description": description,
            "color": color
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
