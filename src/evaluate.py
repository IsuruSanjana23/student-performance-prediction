from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model,X_train, X_test,y_train, y_test):

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_r2_score = r2_score(y_train, train_predictions)
    test_r2_score = r2_score(y_test, test_predictions)

    return train_r2_score, test_r2_score , test_predictions