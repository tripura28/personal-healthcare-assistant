from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)  # ✅ FIXED
CORS(app)

# Load sample data from data.json
with open('data.json') as f:
    data = json.load(f)

@app.route('/pregnant/recommendation', methods=['POST'])
def pregnant_recommendation():
    trimester = request.json.get('trimester')
    rec = data.get('pregnant', {}).get(str(trimester))
    if not rec:
        rec = {"diet": "No recommendation found", "supplements": "", "next_checkup": ""}
    return jsonify(rec)

@app.route('/patient/recommendation', methods=['POST'])
def patient_recommendation():
    condition = request.json.get('condition', '').lower()
    rec = data.get('patients', {}).get(condition)
    if not rec:
        rec = {"medications": "No recommendation found", "diet": "", "exercise": ""}
    return jsonify(rec)

if __name__ == '__main__':  # ✅ FIXED
    app.run(debug=True)
