# Network Traffic Anomaly Detection

This project implements an anomaly detection system for network traffic data using machine learning techniques. It includes training a classification model and deploying it via a Streamlit web application for real-time predictions.

---

## Table of Contents

- Project Overview  
- Features  
- Installation  
- Usage  
- Dataset  
- Model Training  
- Deployment  
- Input Features  
- License  

---

## Project Overview

The goal is to detect anomalies in network traffic by analyzing specific network parameters (e.g., packet counts, octets, errors) and classify whether the traffic is normal or anomalous.

The model is trained on preprocessed network traffic data and then deployed using Streamlit to provide an interactive UI for users to input parameters and get predictions.

---

## Features

- Data preprocessing and feature selection  
- Machine learning model training (e.g., RandomForestClassifier)  
- Model pipeline serialization using joblib  
- Streamlit-based web interface for live prediction  
- Easy customization with input sliders and fields  

---

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/network-traffic-anomaly-detection.git
   cd network-traffic-anomaly-detection

2. Create and activate a virtual environment (Windows):
   python -m venv venv
   .\venv\Scripts\Activate

3. Install dependencies:
   pip install -r requirements.txt

---

## Usage

### Train the model

Make sure your dataset CSV file (e.g., all_data.csv) is in the project directory or update the path accordingly in train_model.py.

Run the training script:

python train_model.py

This will train the model and save the pipeline to models/pipeline.pkl.

### Run the Streamlit app

Activate your environment and start the app:

streamlit run deployment_streamlit_app.py
.\venv\Scripts\Activate
pip install streamlit
streamlit run deployment_streamlit_app.py
                  OR
python -m streamlit run deployment_streamlit_app.py


Open the provided local URL in your browser to access the app interface.

---

## Dataset

- Dataset used: [Describe your dataset or link if public]  
- Features used for training (example subset):
  - ifInOctets11
  - ifOutOctets11
  - tcpInSegs
  - ipOutRequests
  - icmpInEchos
  - and more...

---

## Model Training

The training script train_model.py loads the dataset, preprocesses data, trains a Random Forest classifier, and saves the model pipeline using joblib.

---

## Deployment

The Streamlit app (deployment_streamlit_app.py) loads the saved model pipeline and provides input widgets for users to enter network parameters, then outputs the predicted class (normal/anomalous).

---

## Input Features

The app takes the following input parameters (example):

Feature           | Input Type | Description
------------------|------------|-------------------------------
ifInOctets11      | Number     | Incoming octets on interface 11
ifOutOctets11     | Number     | Outgoing octets on interface 11
tcpInSegs         | Number     | TCP incoming segments
ipOutRequests     | Number     | IP outgoing requests
icmpInEchos       | Number     | ICMP incoming echo messages

*Note: Customize inputs according to your feature set.*

---

## Contact

For questions or suggestions, feel free to open an issue or contact me at nikhilitsme4@gmail.com.

---

Happy Network Anomaly Detecting! 🚀
