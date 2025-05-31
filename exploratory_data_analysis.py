import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/UNSW_NB15_clean.csv')

sns.countplot(x='label', data=df)
plt.title("Normal vs Anomaly")
plt.show()

plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.show()
