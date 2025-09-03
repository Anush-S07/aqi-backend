from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained model (update filename if different)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")  # If you want frontend served here

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Accept JSON or Form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Example: extract features (replace with your actual feature names)
        feature1 = float(data.get("feature1", 0))
        feature2 = float(data.get("feature2", 0))
        feature3 = float(data.get("feature3", 0))
        feature4 = float(data.get("feature4", 0))

        # Put features into array
        features = np.array([[feature1, feature2, feature3, feature4]])

        # Predict
        prediction = model.predict(features)[0]

        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
