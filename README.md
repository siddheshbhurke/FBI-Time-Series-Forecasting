
# FBI Time Series Forecasting

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen)](https://fbi-time-series-forecasting.streamlit.app/)

## 🚨 Project Overview

This project focuses on **forecasting FBI crime patterns** using historical crime data and time series modeling techniques. The objective is to analyze temporal trends and generate future crime predictions to support law enforcement planning and decision-making.

The solution includes:
- Exploratory Data Analysis (EDA)
- Time-based feature engineering
- Machine learning model development and training
- A web application powered by Streamlit for real-time crime prediction

---

## 🧠 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **ML Frameworks**: Scikit-learn, XGBoost
- **Visualization**: Matplotlib, Seaborn
- **Geo-analysis**: GeoPandas, Shapely

---

## 🗂️ Project Structure

```bash
.
├── app.py                         # Streamlit app
├── fbi-crime-prediction-jupyter-file.ipynb  # EDA + model building
├── crime_model.pkl               # Trained ML model
├── model_columns.pkl             # Feature columns used in the model
├── Train.xlsx                    # Training dataset
├── Test.csv                      # Evaluation dataset
├── crime_predictions.csv         # Output predictions
├── monthly-distribution.png      # Trend visualization
├── crime_type_distribution.png   # Crime category distribution
└── requirements.txt              # Dependencies
```

---

## 🚀 Live Demo

Access the deployed web application here:  
👉 [https://fbi-time-series-forecasting.streamlit.app/](https://fbi-time-series-forecasting.streamlit.app/)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/siddheshbhurke/FBI-Time-Series-Forecasting.git
   cd FBI-Time-Series-Forecasting
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app locally**
   ```bash
   streamlit run app.py
   ```

---

## 📊 Features

- Crime type classification and frequency analysis
- Monthly trend and seasonal pattern visualizations
- Time series-based prediction using XGBoost and engineered temporal features
- Model deployed with simple, interactive web UI

---

## 📁 Dataset Description

- Sourced from historical FBI crime reports
- Includes features such as:
  - `TYPE`, `NEIGHBOURHOOD`, `LAT/LONG`
  - Temporal features: `YEAR`, `MONTH`, `DAY`, `HOUR`, etc.

---

## 📌 Future Improvements

- Integration of ARIMA/LSTM for deeper temporal modeling
- Crime heatmaps via geospatial plotting
- Support for user-uploaded datasets
- Model performance evaluation UI

---

## 🤝 Contributing

Contributions are welcome. Fork the repo, create a new branch, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- FBI Open Crime Data
- Open-source Python ecosystem
- Streamlit community
