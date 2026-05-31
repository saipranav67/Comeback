import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# ---------------- Dataset (XOR) ----------------
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# ---------------- Initialization ----------------
np.random.seed(1)

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

W1 = np.random.uniform(size=(input_neurons, hidden_neurons))
b1 = np.random.uniform(size=(1, hidden_neurons))

W2 = np.random.uniform(size=(hidden_neurons, output_neurons))
b2 = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.5
epochs = 5000

print("Training Started...\n")

for epoch in range(epochs):
    
    # Forward Propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)
    
    # Error Calculation
    error = y - final_output
    mse = np.mean(np.square(error))
    
    # Print progress
    if epoch % 500 == 0:
        print(f"Epoch {epoch} | MSE: {mse:.6f}")
    
    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    
    # Weight Updates
    W2 += hidden_output.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

print("\nTraining Completed!\n")

# ---------------- Testing ----------------
print("Final Outputs:\n")

for i in range(len(X)):
    h = sigmoid(np.dot(X[i], W1) + b1)
    o = sigmoid(np.dot(h, W2) + b2)
    
    value = o.item()   # Convert numpy array to scalar
    
    # Apply threshold
    out = 1 if value >= 0.5 else 0
    
    print(f"{X[i]} -> {value:.4f} -> {out}")

