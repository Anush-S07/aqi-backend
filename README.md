🌍 Air Quality Index (AQI) Predictor

This project is a Flask-based web application that predicts the Air Quality Index (AQI) based on key pollutant levels (PM2.5, PM10, CO, SO₂, NO₂, O₃).
It provides both:

🌐 Web interface (HTML form served via Flask)

⚡ REST API endpoint (/predict)

The application is deployed on Render and can also run locally.
----------------------------------------------------------------
📌 Features

🧾 Input pollutant values (PM2.5, PM10, CO, SO₂, NO₂, O₃)

🔮 Predicts AQI value, category, color, and health description

🎨 Simple web UI (templates/index.html + static/style.css)

⚡ REST API available for integration (/predict accepts JSON)

☁️ Easy deployment on Render or any cloud platform

--------------------------------------------------------------

Setup & Installation
🔹 1. Clone the Repository
git clone https://github.com/your-username/aqi-predictor.git
cd aqi-predictor

🔹 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows

🔹 3. Install Dependencies
pip install -r requirements.txt

🔹 4. Run the Application Locally
python app.py


The app will run at:
👉 http://127.0.0.1:5000

