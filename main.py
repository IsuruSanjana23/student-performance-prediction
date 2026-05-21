import pandas as pd

df = pd.read_csv('D:\Projects\student-performance-prediction\data\data.csv')

"""
print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())
"""

from src.preprocess import load_and_preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.predict import predict_grade , predict_grade_input_data
from src.visualize import plot_predictions

X_train,X_test,y_train,y_test = load_and_preprocess_data()

#print("X_train shape:", X_train.shape)
#print("X_test shape:", X_test.shape)

#model = train_model(X_train, X_test, y_train, y_test)

#train_r2 , test_r2 , predictions = evaluate_model(model, X_train, X_test, y_train, y_test)


#print(f"Train R2: {train_r2:.2f}")
#print(f"Test r2: {test_r2:.2f}")

#plot_predictions(y_test,predictions)

#predicted_grade = predict_grade()
#print(f"Predicted Grade: {predicted_grade:.2f}")


try:
    predictions  = predict_grade_input_data()
    print(f"Predicted Grade: {predictions:.2f}")
except Exception as e:
    print("Error during prediction:", str(e))