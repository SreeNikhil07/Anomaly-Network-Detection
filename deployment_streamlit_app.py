import streamlit as st
import joblib
import pandas as pd
import os

# Load model
MODEL_PATH = "models/pipeline.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("Trained model not found. Please train the model first.")
    st.stop()

pipeline = joblib.load(MODEL_PATH)

# Title
st.title("Network Traffic Anomaly Detection")

# Instructions
st.write("Enter network traffic feature values below:")

# Input fields — must match the model's training features
ifInOctets11 = st.number_input("ifInOctets11", value=1000)
ifOutOctets11 = st.number_input("ifOutOctets11", value=1000)
tcpInSegs = st.number_input("tcpInSegs", value=500)
tcpOutSegs = st.number_input("tcpOutSegs", value=500)
ipInReceives = st.number_input("ipInReceives", value=1500)
ipOutRequests = st.number_input("ipOutRequests", value=1600)

# Create input DataFrame
input_data = {
    'ifInOctets11': [ifInOctets11],
    'ifOutOctets11': [ifOutOctets11],
    'tcpInSegs': [tcpInSegs],
    'tcpOutSegs': [tcpOutSegs],
    'ipInReceives': [ipInReceives],
    'ipOutRequests': [ipOutRequests]
}
input_df = pd.DataFrame(input_data)

# Prediction
if st.button("Predict"):
    prediction = pipeline.predict(input_df)[0]
    st.success(f"Predicted Class: **{prediction}**")
