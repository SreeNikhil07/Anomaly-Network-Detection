import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\HP\Desktop\Network\all_data (3).csv')

# Drop irrelevant columns
df = df.drop(['id', 'proto', 'service', 'state'], axis=1, errors='ignore')

# Label encode (modify this if your label column name is different)
df['label'] = df['label'].apply(lambda x: 0 if x == 'Normal' else 1)

# Save cleaned dataset
df.to_csv('dataset/UNSW_NB15_clean.csv', index=False)
