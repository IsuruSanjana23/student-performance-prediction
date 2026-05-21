import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, X_test, y_train, y_test):
    #model = LinearRegression()
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "models/student_score_prediction_RandomForestRegressor_model.joblib")

    return model