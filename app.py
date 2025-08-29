from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)  # Corrected __name__
CORS(app)              # Enables Cross-Origin requests

# Load sample data
with open('data.json') as f:
    data = json.load(f)

@app.route('/pregnant/recommendation', methods=['POST'])
def pregnant_recommendation():
    trimester = request.json.get('trimester')
    print("Received trimester:", trimester)
    rec = data.get('pregnant', {}).get(str(trimester))
    if not rec:
        rec = {"diet":"No recommendation found","supplements":"","next_checkup":""}
    return jsonify(rec)

@app.route('/patient/recommendation', methods=['POST'])
def patient_recommendation():
    condition = request.json.get('condition', '').lower()
    print("Received condition:", condition)
    rec = data.get('patients', {}).get(condition)
    if not rec:
        rec = {"medications":"No recommendation found","diet":"","exercise":""}
    return jsonify(rec)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
