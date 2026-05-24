import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)
n = 20000
n_fraud = int(n * 0.3)
n_legit = n - n_fraud

legit = pd.DataFrame({
    'Transaction Amount': np.random.uniform(0.0, 0.4, n_legit),
    'Transaction Frequency': np.random.uniform(0.1, 0.5, n_legit),
    'Recipient Blacklist Status': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Device Fingerprinting': np.random.choice([0, 1], n_legit, p=[0.9, 0.1]),
    'VPN or Proxy Usage': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Behavioral Biometrics': np.random.uniform(0.0, 0.5, n_legit),
    'Time Since Last Transaction': np.random.uniform(0.3, 1.0, n_legit),
    'Social Trust Score': np.random.uniform(0.5, 1.0, n_legit),
    'Account Age': np.random.uniform(0.3, 1.0, n_legit),
    'High-Risk Transaction Times': np.random.choice([0, 1], n_legit, p=[0.9, 0.1]),
    'Past Fraudulent Behavior Flags': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Location-Inconsistent Transactions': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Normalized Transaction Amount': np.random.uniform(0.0, 0.4, n_legit),
    'Transaction Context Anomalies': np.random.uniform(0.0, 0.3, n_legit),
    'Fraud Complaints Count': np.random.uniform(0.0, 0.1, n_legit),
    'Merchant Category Mismatch': np.random.choice([0, 1], n_legit, p=[0.9, 0.1]),
    'User Daily Limit Exceeded': np.random.choice([0, 1], n_legit, p=[0.9, 0.1]),
    'Recent High-Value Transaction Flags': np.random.choice([0, 1], n_legit, p=[0.9, 0.1]),
    'Recipient Verification Status_suspicious': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Recipient Verification Status_verified': np.random.choice([0, 1], n_legit, p=[0.2, 0.8]),
    'Geo-Location Flags_normal': np.random.choice([0, 1], n_legit, p=[0.1, 0.9]),
    'Geo-Location Flags_unusual': np.random.choice([0, 1], n_legit, p=[0.95, 0.05]),
    'Label': 0
})

fraud = pd.DataFrame({
    'Transaction Amount': np.random.uniform(0.6, 1.0, n_fraud),
    'Transaction Frequency': np.random.uniform(0.6, 1.0, n_fraud),
    'Recipient Blacklist Status': np.random.choice([0, 1], n_fraud, p=[0.2, 0.8]),
    'Device Fingerprinting': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'VPN or Proxy Usage': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'Behavioral Biometrics': np.random.uniform(0.6, 1.0, n_fraud),
    'Time Since Last Transaction': np.random.uniform(0.0, 0.3, n_fraud),
    'Social Trust Score': np.random.uniform(0.0, 0.3, n_fraud),
    'Account Age': np.random.uniform(0.0, 0.2, n_fraud),
    'High-Risk Transaction Times': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'Past Fraudulent Behavior Flags': np.random.choice([0, 1], n_fraud, p=[0.2, 0.8]),
    'Location-Inconsistent Transactions': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'Normalized Transaction Amount': np.random.uniform(0.6, 1.0, n_fraud),
    'Transaction Context Anomalies': np.random.uniform(0.6, 1.0, n_fraud),
    'Fraud Complaints Count': np.random.uniform(0.5, 1.0, n_fraud),
    'Merchant Category Mismatch': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'User Daily Limit Exceeded': np.random.choice([0, 1], n_fraud, p=[0.2, 0.8]),
    'Recent High-Value Transaction Flags': np.random.choice([0, 1], n_fraud, p=[0.3, 0.7]),
    'Recipient Verification Status_suspicious': np.random.choice([0, 1], n_fraud, p=[0.2, 0.8]),
    'Recipient Verification Status_verified': np.random.choice([0, 1], n_fraud, p=[0.8, 0.2]),
    'Geo-Location Flags_normal': np.random.choice([0, 1], n_fraud, p=[0.8, 0.2]),
    'Geo-Location Flags_unusual': np.random.choice([0, 1], n_fraud, p=[0.2, 0.8]),
    'Label': 1
})

data = pd.concat([legit, fraud]).sample(frac=1, random_state=42).reset_index(drop=True)
X = data.drop('Label', axis=1)
y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print('Accuracy:', model.score(X_test, y_test))
joblib.dump(model, 'best_rf_model.pkl')
print('Model saved!')