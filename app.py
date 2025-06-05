import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# --- UI Configuration ---
st.set_page_config(page_title="Crime Forecasting Dashboard", layout="wide")
st.title("\U0001F52E FBI Crime Incident Forecaster")

# --- Load model and metadata ---
model = joblib.load('crime_model.pkl')
columns = joblib.load('model_columns.pkl')  # list of training columns

# --- Input Form ---
st.sidebar.header("Input Parameters")

# Month and year input
year = st.sidebar.selectbox("Year", list(range(2003, 2026)))
month = st.sidebar.selectbox("Month", list(range(1, 13)))

# Crime type input
crime_type = st.sidebar.selectbox("Crime Type", [
    'Break and Enter Commercial',
    'Break and Enter Residential/Other',
    'Mischief',
    'Other Theft',
    'Theft from Vehicle',
    'Theft of Bicycle',
    'Theft of Vehicle',
    'Vehicle Collision or Pedestrian Struck (with Injury)'  # Add all trained types
])

# --- Preprocess Input ---
input_df = pd.DataFrame([[year, month, crime_type]], columns=['YEAR', 'MONTH', 'TYPE'])
input_encoded = pd.get_dummies(input_df, columns=['TYPE'])
input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

# --- Predict ---
if st.sidebar.button("Predict Incident Count"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"\nPredicted Incident Count for {crime_type} in {month}/{year}: {prediction:.0f}")

# --- Display Pre-generated Chart Image ---
st.subheader("Crime Type Distribution (Training Data)")
try:
    st.image("crime_type_distribution.png", caption="Crime Type Distribution", use_container_width=True)
except Exception as e:
    st.warning(f"Could not display chart image: {e}")

st.subheader("Monthly Crime Distribution (Training Data)")
try:
    st.image("monthly-distribution.png", caption="Monthly Crime Distribution", use_container_width=True)
except Exception as e:
    st.warning(f"Could not display chart image: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("**Note**: This prediction is based on historical trends and does not account for real-time factors.")
