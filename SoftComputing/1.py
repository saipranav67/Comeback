import numpy as np

# Adaline Training Function
def adaline(X, T, lr=0.1, epochs=15):
    # Initialize weights and bias
    w = np.random.rand(X.shape[1])
    b = np.random.rand(1)

    print("Initial Weights:", w)
    print("Initial Bias:", b)

    # Training
    for epoch in range(epochs):
        total_error = 0
        for i in range(len(X)):
            # Net input
            y_in = np.dot(w, X[i]) + b

            # Error
            error = T[i] - y_in

            # Update weights and bias
            w = w + lr * error * X[i]
            b = b + lr * error

            # Sum of squared error
            total_error += error**2

        print(f"Epoch {epoch+1}, Error: {total_error}")

    return w, b


# OR Gate Data (Bipolar)
X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

T = np.array([1, 1, 1, -1])


# Training the model
w, b = adaline(X, T, lr=0.1, epochs=15)

print("\nFinal Weights:", w)
print("Final Bias:", b)


# Prediction Function
def predict(X, w, b):
    outputs = []
    for i in range(len(X)):
        y_in = np.dot(w, X[i]) + b
        y = 1 if y_in >= 0 else -1   # Activation
        outputs.append(y)
    return outputs


# Testing the model
output = predict(X, w, b)

print("\nPredicted Outputs:", output)
print("Expected Outputs :", T)