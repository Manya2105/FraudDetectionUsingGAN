from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load('best_rf_model.pkl')

@app.route('/')
def home():
    return jsonify({"status": "SafePayAI API is running", "model_loaded": True})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
        fraud_prob = probability[1]

        return jsonify({
            "prediction": "Fraud" if prediction == 1 else "Not Fraud",
            "is_fraud": bool(prediction == 1),
            "fraud_probability": round(fraud_prob, 4),
            "confidence": round(max(probability), 4)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)