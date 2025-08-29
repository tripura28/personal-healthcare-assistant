from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load datasets
maternal_df = pd.read_csv('data/Maternal_health.csv')
diabetes_df = pd.read_csv('data/Diabetes.csv')
breast_cancer_df = pd.read_csv('data/Breast_cancer.csv')

# Helper functions
def get_pregnancy_recommendation(trimester):
    row = maternal_df[maternal_df['gestational_age_weeks'] // 13 + 1 == int(trimester)]
    if not row.empty:
        return {
            "diet": "Leafy Greens, Whole Grains",
            "supplements": "Iron, Folic Acid",
            "next_checkup": "2025-09-15"
        }
    else:
        return {"diet": "No recommendation found", "supplements": "", "next_checkup": ""}

def get_patient_recommendation(condition):
    if condition.lower() == "diabetes":
        return {"medications": "Metformin, Insulin", "diet": "Low sugar, High fiber", "exercise": "30 min walk"}
    elif condition.lower() == "breast cancer" or condition.lower() == "tumor":
        return {"medications": "Chemotherapy", "diet": "High protein", "exercise": "Light walk"}
    else:
        return {"medications": "No recommendation found", "diet": "", "exercise": ""}

# API routes
@app.route('/pregnant/recommendation', methods=['POST'])
def pregnant_recommendation():
    data = request.get_json()
    trimester = data.get('trimester')
    result = get_pregnancy_recommendation(trimester)
    return jsonify(result)

@app.route('/patient/recommendation', methods=['POST'])
def patient_recommendation():
    data = request.get_json()
    condition = data.get('condition')
    result = get_patient_recommendation(condition)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
