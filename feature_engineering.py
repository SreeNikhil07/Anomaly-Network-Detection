from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv('dataset/UNSW_NB15_clean.csv')
X = df.drop('label', axis=1)
y = df['label']

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pd.DataFrame(X_scaled).to_csv('dataset/X_scaled.csv', index=False)
y.to_csv('dataset/y.csv', index=False)
