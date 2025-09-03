# 🌍 Air Quality Index (AQI) Predictor

This project is a **Flask-based web application** that predicts the **Air Quality Index (AQI)** based on key pollutant levels (PM2.5, PM10, CO, SO₂, NO₂, O₃).
It provides both:

* 🌐 **Web interface** (HTML form served via Flask)
* ⚡ **REST API** endpoint (`/predict`)

The application is deployed on **Render** and can also run locally.

---

## 📌 Features

* 🧾 Input pollutant values (PM2.5, PM10, CO, SO₂, NO₂, O₃)
* 🔮 Predicts **AQI value, category, color, and health description**
* 🎨 Simple web UI (`templates/index.html` + `static/style.css`)
* ⚡ REST API available for integration (`/predict` accepts JSON)
* ☁️ Easy deployment on **Render** or any cloud platform

---

## 📂 Project Structure

```
AQI-Predictor/
 ├── app.py                 # Flask backend
 ├── requirements.txt       # Dependencies
 ├── model.pkl              # (Optional) Saved ML model if used
 ├── templates/
 │    └── index.html        # Frontend HTML form
 ├── static/
 │    └── style.css         # CSS for frontend
 └── README.md              # Project documentation
```

---

## ⚙️ Setup & Installation

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/aqi-predictor.git
cd aqi-predictor
```

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Run the Application Locally

```bash
python app.py
```

The app will run at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Usage

### 🔹 Web Interface

1. Open [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. Enter pollutant values
3. Click **Predict AQI**
4. Get results with **AQI value, category, description, and color**

### 🔹 API Endpoint

Send a POST request to `/predict` with pollutant data:

#### Example (PowerShell / Windows)

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"pm25":35,"pm10":60,"co":800,"so2":20,"no2":40,"o3":30}'
```

#### Example (cURL / Linux/Mac)

```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"pm25":35,"pm10":60,"co":800,"so2":20,"no2":40,"o3":30}'
```

#### Example Response

```json
{
  "aqi": 60.01,
  "category": "Moderate",
  "color": "yellow",
  "description": "Breathing discomfort for sensitive groups"
}
```

---

## ☁️ Deployment on Render

1. Push code to GitHub
2. Go to [Render](https://render.com)
3. Create a **new Web Service**

   * Connect to your GitHub repo
   * Set build command:

     ```bash
     pip install -r requirements.txt
     ```
   * Set start command:

     ```bash
     gunicorn app:app
     ```
4. Deploy 🎉

👉 Your app will be available at `https://your-app-name.onrender.com`

* Web UI → `/`
* API → `/predict`

---

## 📦 Requirements

Your `requirements.txt` should include at least:

```
Flask
gunicorn
```

(plus any other libraries you used for AQI calculation / ML model)

---

## 👨‍💻 Author

Developed by **\[Anush S]**
📧 Contact: [anushmv2001@gmail.com](mailto:your.email@example.com)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

✅ This version will render code sections properly on GitHub.

Do you also want me to **write a ready-to-use `requirements.txt` and final clean `app.py`** so you can just push to GitHub and deploy without touching anything?
