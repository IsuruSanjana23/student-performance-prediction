from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://student-performance-prediction-p14b1mgzl.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    socioeconomic_score: float
    study_hours: float
    sleep_hours: float
    attendance: float

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Student Grade Predictor API", "status": "healthy"}

# Models endpoint if needed
@app.get("/v1/models")
def list_models():
    return {
        "models": ["student_score_prediction_RandomForestRegressor_model"],
        "endpoints": {
            "predict": "/predict",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }

# Your predict endpoint
@app.post("/predict")
def predict_grade_api(student_data: StudentData):
    try:
        model = joblib.load(
            "models/student_score_prediction_RandomForestRegressor_model.joblib"
        )

        study_score = (student_data.study_hours * student_data.attendance)

        new_student = pd.DataFrame({
            'Socioeconomic Score': [student_data.socioeconomic_score],
            'Study Hours': [student_data.study_hours],
            'Sleep Hours': [student_data.sleep_hours],
            'Attendance (%)': [student_data.attendance],
            'Study Score': [study_score]
        })

        prediction = model.predict(new_student)

        return {
            "predicted_grade": float(prediction[0]),
            "status": "success",
            "message": "Prediction completed successfully"
        }

    except Exception as e:
        return {
            "error": str(e),
            "status": "error",
            "message": "Prediction failed"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)