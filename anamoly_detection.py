import pandas as pd
import joblib

df = pd.read_csv('dataset/UNSW_NB15_clean.csv')
X = pd.read_csv('dataset/X_scaled.csv')
model = joblib.load('models/isolation_forest_model.pkl')

preds = model.predict(X)
df['Anomaly'] = ['Anomaly' if x == -1 else 'Normal' for x in preds]

df[df['Anomaly'] == 'Anomaly'].head()
