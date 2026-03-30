import numpy as np

# Activation functions
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2

# XOR Data (Bipolar)
X = np.array([
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
], dtype=float)

T = np.array([-1, 1, 1, -1], dtype=float)

# Initialize weights
np.random.seed(42)
w_hidden = np.random.uniform(-0.5, 0.5, (2, 2))
b_hidden = np.zeros(2)

w_output = np.random.uniform(-0.5, 0.5, 2)
b_output = 0.0

# Training parameters
lr = 0.5
epochs = 5000

# Training using backpropagation
for epoch in range(1, epochs + 1):
    total_error = 0
    for x, t in zip(X, T):

        # Forward pass
        hidden_in = np.dot(x, w_hidden) + b_hidden
        hidden_out = tanh(hidden_in)

        y_in = np.dot(hidden_out, w_output) + b_output
        y_out = tanh(y_in)

        # Error
        error = t - y_out
        total_error += error ** 2

        # Backward pass
        delta_out = error * tanh_derivative(y_in)

        # Update output weights
        w_output += lr * delta_out * hidden_out
        b_output += lr * delta_out

        # Update hidden weights
        for i in range(w_hidden.shape[1]):
            delta_hidden = delta_out * w_output[i] * tanh_derivative(hidden_in[i])
            w_hidden[:, i] += lr * delta_hidden * x
            b_hidden[i] += lr * delta_hidden

    # Print error every 500 epochs
    if epoch % 500 == 0:
        mse = total_error / len(X)
        print(f"Epoch {epoch} | MSE: {mse:.6f}")

# Testing
print("\nTesting XOR:")
for x, t in zip(X, T):
    hidden_out = tanh(np.dot(x, w_hidden) + b_hidden)
    y_out = tanh(np.dot(hidden_out, w_output) + b_output)
    y = 1 if y_out >= 0 else -1
    print(f"Input: {x} → Output: {y}, Expected: {int(t)}")