from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Model file not found. Please ensure 'model.pkl' is in the same directory.")
    model = None

FEATURE_NAMES = [
    'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender',
    'HourlyRate', 'JobInvolvement', 'JobRole', 'JobSatisfaction',
    'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'OverTime', 'PercentSalaryHike', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsInCurrentRole', 'YearsSinceLastPromotion'
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        
        form_data = request.get_json()
        
        features = []
        for feature_name in FEATURE_NAMES:
            value = form_data.get(feature_name)

            features.append(float(value))
        
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0]
        
        attrition_status = "Will Leave" if prediction == 0.95 else "Will Stay"
        confidence = max(probability) * 100
        
        return jsonify({
            'prediction': attrition_status,
            'confidence': round(confidence, 2),
            'probability_stay': round(probability[0] * 100, 2),
            'probability_leave': round(probability[1] * 100, 2)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
