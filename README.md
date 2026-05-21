# Student Performance Prediction

A machine learning project that predicts student grades based on various socioeconomic and academic factors. This system uses a Random Forest Regressor model to forecast student performance with high accuracy.

## 📋 Project Overview

This project builds a predictive model to estimate student grades based on key performance indicators including study habits, attendance, sleep patterns, and socioeconomic factors. The model can be used for:
- Identifying at-risk students
- Personalizing academic interventions
- Understanding factors that influence academic success
- Making predictions for new student data

## ✨ Features

- **Data Preprocessing**: Automated data loading and feature engineering
- **Model Training**: Random Forest Regressor with 100 estimators for robust predictions
- **Model Evaluation**: R² score calculation for both training and test datasets
- **Visualization**: Actual vs Predicted scatter plots for model performance analysis
- **Interactive Predictions**: Get predictions for custom student data via user input
- **Model Persistence**: Trained models saved as `.joblib` files for reuse

## 📁 Project Structure

```
student-performance-prediction/
├── main.py                          # Main entry point
├── requirements.txt                 # Project dependencies
├── README.md                        # This file
├── data/
│   └── data.csv                     # Student performance dataset
├── models/
│   ├── student_score_prediction_model.joblib
│   └── student_score_prediction_RandomForestRegressor_model.joblib
└── src/
    ├── preprocess.py               # Data loading and preprocessing
    ├── train.py                    # Model training
    ├── evaluate.py                 # Model evaluation metrics
    ├── predict.py                  # Prediction functions
    └── visualize.py                # Visualization utilities
```

## 📊 Dataset Features

The model uses the following features to predict student grades:

| Feature | Description |
|---------|-------------|
| **Socioeconomic Score** | Student's socioeconomic background (0-1 scale) |
| **Study Hours** | Number of hours spent studying per week |
| **Sleep Hours** | Average hours of sleep per night |
| **Attendance (%)** | Percentage of classes attended |
| **Study Score** | Derived feature: Study Hours × Attendance (%) |

**Target Variable**: Student Grades

## 🤖 Model Details

- **Algorithm**: Random Forest Regressor
- **Parameters**: 
  - n_estimators: 100
  - random_state: 42
- **Data Split**: 80% training, 20% testing
- **Cross-validation**: train_test_split with reproducible random_state

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or download the project**:
   ```bash
   cd student-performance-prediction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install additional ML dependencies**:
   ```bash
   pip install scikit-learn joblib
   ```

4. **Ensure the data file exists** in the `data/` directory:
   - `data.csv` - Contains the student performance dataset

## 📖 Usage

### Option 1: Make Predictions with Interactive Input

Run the main script and enter student data when prompted:

```bash
python main.py
```

You'll be asked to provide:
- Socioeconomic Score (0-1)
- Study Hours
- Sleep Hours  
- Attendance (%)

The system will output the predicted grade.

### Option 2: Train a New Model

Uncomment lines in `main.py` to train and evaluate a model:

```python
from src.train import train_model
from src.evaluate import evaluate_model

model = train_model(X_train, X_test, y_train, y_test)
train_r2, test_r2, predictions = evaluate_model(model, X_train, X_test, y_train, y_test)

print(f"Train R2: {train_r2:.2f}")
print(f"Test R2: {test_r2:.2f}")
```

### Option 3: Visualize Model Performance

```python
from src.visualize import plot_predictions

plot_predictions(y_test, predictions)
```

## 📦 Dependencies

| Package | Version |
|---------|---------|
| numpy | ~2.4.4 |
| pandas | ~3.0.2 |
| matplotlib | ~3.10.9 |
| scikit-learn | Latest |
| joblib | Latest |

Install all dependencies with:
```bash
pip install -r requirements.txt
pip install scikit-learn joblib
```

## 📈 Module Descriptions

### `src/preprocess.py`
- Loads student data from CSV
- Creates derived feature (Study Score = Study Hours × Attendance)
- Splits data into training and testing sets (80/20 split)
- Returns: `X_train, X_test, y_train, y_test`

### `src/train.py`
- Trains a Random Forest Regressor model
- Saves the trained model as a joblib file
- Returns the trained model object

### `src/evaluate.py`
- Calculates R² scores for training and test data
- Generates predictions on test set
- Returns: `train_r2_score, test_r2_score, test_predictions`

### `src/predict.py`
- `predict_grade()`: Makes a prediction for a predefined student
- `predict_grade_input_data()`: Interactive function to get user input and make predictions

### `src/visualize.py`
- Plots actual vs predicted grades
- Shows perfect prediction line for reference
- Generates scatter plot with matplotlib

## 🎯 Example Workflow

```python
# 1. Load and preprocess data
from src.preprocess import load_and_preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_predictions

X_train, X_test, y_train, y_test = load_and_preprocess_data()

# 2. Train the model
model = train_model(X_train, X_test, y_train, y_test)

# 3. Evaluate performance
train_r2, test_r2, predictions = evaluate_model(model, X_train, X_test, y_train, y_test)
print(f"Model R² Score: {test_r2:.4f}")

# 4. Visualize results
plot_predictions(y_test, predictions)
```

## 🔍 Model Performance Metrics

- **R² Score (Coefficient of Determination)**:
  - Measures how well the model explains variance in grades
  - Range: 0 to 1 (higher is better)
  - 1.0 = Perfect predictions
  - 0.0 = Model performs as well as a baseline

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: data.csv` | Ensure `data/data.csv` exists in the project directory |
| `ModuleNotFoundError: sklearn` | Run `pip install scikit-learn` |
| `Model not found` | Train a new model or ensure model files exist in `models/` directory |
| Input validation errors | Ensure all input values are numeric and within valid ranges |

## 🚦 Next Steps & Future Improvements

- [ ] Hyperparameter tuning (GridSearchCV, RandomizedSearchCV)
- [ ] Feature scaling and normalization for better performance
- [ ] Cross-validation for more robust evaluation
- [ ] Ensemble methods (Gradient Boosting, XGBoost)
- [ ] Feature importance analysis
- [ ] REST API for model serving
- [ ] Web interface for predictions
- [ ] Data validation and comprehensive error handling
- [ ] Automated model retraining pipeline
- [ ] Support for handling missing/incomplete data
- [ ] Model interpretability analysis

## 📝 Implementation Notes

- The model uses a fixed random_state=42 for reproducibility
- Study Score is calculated as: Study Hours × Attendance (%)
- All features are used without normalization (Random Forests are scale-invariant)
- Model persistence allows loading trained models without retraining
- The project divides the dataset into features (X) and target (y)

## 👨‍💻 Author

Student Performance Prediction ML Project

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated**: May 21, 2026

