from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import joblib

X = pd.read_csv('dataset/X_scaled.csv')
y = pd.read_csv('dataset/y.csv')

model = joblib.load('models/isolation_forest_model.pkl')

preds = model.predict(X)
preds = [1 if p == -1 else 0 for p in preds]

print(confusion_matrix(y, preds))
print(classification_report(y, preds))
