import matplotlib.pyplot as plt

def plot_predictions(y_test , predictions):

    plt.figure(figsize=(8,6))

    # Actual vs Predicted points
    plt.scatter(
        y_test,
        predictions,
        color='red',
        alpha=0.7,
        label='Predictions'
    )

    # Perfect prediction line
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color='blue',
        linewidth=2,
        label='Perfect Prediction'
    )

    plt.xlabel("Actual Grade")
    plt.ylabel("Predicted Grade")

    plt.title("Actual vs Predicted Grade")

    plt.legend()

    plt.show()