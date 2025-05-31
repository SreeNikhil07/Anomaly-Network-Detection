import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import os

# Fix the file path using a raw string to avoid escape issues
DATA_FILE = r"C:\Users\HP\Desktop\Network\all_data (3).csv"
TARGET_COLUMN = "class"
MODEL_PATH = "models/pipeline.pkl"

# Selected features
selected_features = [
    'ifInOctets11',
    'ifOutOctets11',
    'tcpInSegs',
    'tcpOutSegs',
    'ipInReceives',
    'ipOutRequests'
]

# Check if the dataset exists
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"❌ Dataset not found at: {DATA_FILE}")

# Load data
df = pd.read_csv(DATA_FILE)

# Ensure target column exists
if TARGET_COLUMN not in df.columns:
    raise ValueError(f"Target column '{TARGET_COLUMN}' not found in dataset columns: {df.columns.tolist()}")

# Ensure selected features exist
missing = [col for col in selected_features if col not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

# Split features and target
X = df[selected_features]
y = df[TARGET_COLUMN]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[('num', StandardScaler(), selected_features)],
    remainder='drop'
)

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Create models folder if not exists
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

# Train and save
pipeline.fit(X, y)
joblib.dump(pipeline, MODEL_PATH)
print(f"✅ Model trained and saved to {MODEL_PATH}")
