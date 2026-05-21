import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_preprocess_data():
    df = pd.read_csv("./data/data.csv")

    df["Study Score"] = (df["Study Hours"] * df["Attendance (%)"])

    #features
    X = df[[
        'Socioeconomic Score',
        'Study Hours',
        'Sleep Hours',
        'Attendance (%)',
        'Study Score'
    ]]

    #Label
    y = df['Grades']

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train,X_test,y_train,y_test