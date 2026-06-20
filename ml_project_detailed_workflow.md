# Student Performance Prediction System --- Detailed Workflow Guide

# 1. Define Problem

## Goal

Predict student grades using student-related information.

## Question

Can we predict:

-   Grades

Using:

-   Socioeconomic Score
-   Study Hours
-   Sleep Hours
-   Attendance

------------------------------------------------------------------------

# 2. Collect Dataset

## What we did

Obtained a Student Performance dataset.

## Why

Machine learning requires data to learn patterns.

Dataset columns:

-   Socioeconomic Score
-   Study Hours
-   Sleep Hours
-   Attendance (%)
-   Grades

------------------------------------------------------------------------

# 3. Load and Inspect Dataset

## What we did

Loaded CSV using:

pd.read_csv()

Checked:

df.head() df.info() df.describe() df.columns df.isnull().sum()

## Why

To understand:

-   Data shape
-   Missing values
-   Column names
-   Data ranges

------------------------------------------------------------------------

# 4. Check Missing Values

## What we did

Used:

df.isnull().sum()

Result:

No missing values found.

## Why

Missing values can break models.

Possible fixes if present:

-   Remove rows
-   Replace with mean
-   Replace with median

------------------------------------------------------------------------

# 5. Select Features and Labels

## What we did

Features (X):

-   Socioeconomic Score
-   Study Hours
-   Sleep Hours
-   Attendance (%)

Label (Y):

-   Grades

## Why

Features: Inputs

Label: Prediction target

Workflow:

Features ↓ Model ↓ Prediction

------------------------------------------------------------------------

# 6. Split Dataset

## What we did

Used:

train_test_split()

Split:

80% Training

20% Testing

random_state=42

## Why

Training: Learn patterns

Testing: Evaluate unseen data

------------------------------------------------------------------------

# 7. Train Initial Model

## What we did

Used:

LinearRegression()

Training:

model.fit(X_train,y_train)

## Why

Predict numerical values.

Grades are numbers.

------------------------------------------------------------------------

# 8. Evaluate Initial Model

## What we did

Metrics:

MAE R²

Results:

MAE = 19.27

R² = 0.7447

## Why

MAE:

Average prediction error

R²:

How much variation model explains

------------------------------------------------------------------------

# 9. Make Predictions

## What we did

Created:

new_student

Used:

model.predict()

## Problem Found

Prediction:

898

Actual range:

32--91

## Cause

Wrong feature range:

Socioeconomic Score = 70

Correct:

0--1

## Lesson

Prediction data must follow same scale as training data.

------------------------------------------------------------------------

# 10. Save Model

## What we did

Used:

joblib.dump()

Saved:

models/student_model.pkl

## Why

Without saving:

Train every time

With saving:

Load → Predict

------------------------------------------------------------------------

# 11. Feature Engineering

## What we did

Created:

Study Score

Formula:

Study Hours × Attendance

## Why

Create smarter information from existing features.

Results:

MAE:

19.27 → 17.85

R²:

0.7447 → 0.7635

------------------------------------------------------------------------

# 12. Retrain and Compare

## What we did

Retrained model after adding new feature.

Compared:

Previous metrics

vs

New metrics

## Why

Determine whether changes improved performance.

------------------------------------------------------------------------

# 13. Try Stronger Algorithm

## What we did

Changed:

LinearRegression()

to:

RandomForestRegressor()

## Why

Random Forest:

-   Handles nonlinear patterns
-   Often stronger than linear models

Results:

MAE = 1.54

R² = 0.9796

------------------------------------------------------------------------

# 14. Check Overfitting

## What we did

Compared:

Train R²

Test R²

Results:

Train = 1.00

Test = 0.98

## Why

Large difference:

Overfitting

Small difference:

Good generalization

------------------------------------------------------------------------

# 15. Visualize Results

## What we did

Created:

Actual vs Predicted graph

Used:

plt.scatter()

Added:

Perfect prediction line

y = x

## Why

Points close to line:

Good predictions

Points far away:

Large errors

------------------------------------------------------------------------

# 16. Push Project To GitHub

## What we did

Commands:

git init

git add .

git commit -m "Initial ML Project"

git push

Added:

.gitignore

Ignored:

venv/ .idea/ **pycache**/ \*.pkl

## Why

Keep repository clean and portfolio-ready

------------------------------------------------------------------------

# Reusable Future ML Workflow

Define Problem ↓ Collect Data ↓ Load Data ↓ Inspect Data ↓ Clean Data ↓
Feature Engineering ↓ Select X and Y ↓ Split Dataset ↓ Train Model ↓
Evaluate ↓ Improve ↓ Check Overfitting ↓ Save Model ↓ Visualize ↓
GitHub/Deploy
