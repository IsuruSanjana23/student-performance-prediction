import pandas as pd
import joblib

def predict_grade():

    model = joblib.load("models/student_score_prediction_RandomForestRegressor_model.joblib")

    new_student = pd.DataFrame({
        'Socioeconomic Score': [0.7],
        'Study Hours': [8],
        'Sleep Hours': [7],
        'Attendance (%)': [90],
    })

    new_student['Study Score'] = new_student['Study Hours'] * new_student['Socioeconomic Score']

    predictions = model.predict(new_student)

    return predictions[0]

def predict_grade_input_data():
    model = joblib.load("models/student_score_prediction_RandomForestRegressor_model.joblib")

    social_economic_score = float(input("Socioeconomic Score (0-1): "))
    study_hours = float(input("Study Hours : "))
    sleep_hours = float(input("Sleep Hours : "))
    attendance = float(input("Attendance (%): "))
    study_score = (study_hours*attendance)

    new_student = pd.DataFrame({
        'Socioeconomic Score': [social_economic_score],
        'Study Hours': [study_hours],
        'Sleep Hours': [sleep_hours],
        'Attendance (%)': [attendance],
        'Study Score': [study_score]
    })

    predictions = model.predict(new_student)

    return predictions[0]

def predict_grade_api(
    socioeconomic_score: float,
    study_hours: float,
    sleep_hours: float,
    attendance: float
):
    model = joblib.load(
        "models/student_score_prediction_RandomForestRegressor_model.joblib"
    )

    study_score = (study_hours * attendance)

    new_student = pd.DataFrame({
        'Socioeconomic Score': [socioeconomic_score],
        'Study Hours': [study_hours],
        'Sleep Hours': [sleep_hours],
        'Attendance (%)': [attendance],
        'Study Score': [study_score]
    })

    prediction = model.predict(new_student)

    return float(prediction[0])