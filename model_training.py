from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

X = pd.read_csv('dataset/X_scaled.csv')

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

joblib.dump(model, 'models/isolation_forest_model.pkl')
