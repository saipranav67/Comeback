import numpy as np

# Activation function (bipolar)
def activation(z):
    return 1 if z >= 0 else -1

# Madaline Network for XOR
def madaline_xor(X, T, lr=0.5, epochs=10):
    # Initialize weights (as assumed)
    w11, w21, b1 = 0.05, 0.2, 0.3
    w12, w22, b2 = 0.1, 0.2, 0.15
    v1, v2, b3 = 0.5, 0.5, 0.5

    for epoch in range(epochs):
        print(f"\nEpoch {epoch+1}")
        for i in range(len(X)):
            x1, x2 = X[i]
            t = T[i]

            # Hidden layer
            zin1 = b1 + x1*w11 + x2*w21
            zin2 = b2 + x1*w12 + x2*w22

            z1 = activation(zin1)
            z2 = activation(zin2)

            # Output layer
            yin = b3 + z1*v1 + z2*v2
            y = activation(yin)

            print(f"Input: {X[i]}, Output: {y}, Target: {t}")

            # Weight update if error exists
            if y != t:
                # Update hidden layer weights
                w11 += lr * (t - zin1) * x1
                w21 += lr * (t - zin1) * x2
                w12 += lr * (t - zin2) * x1
                w22 += lr * (t - zin2) * x2

                # Update biases
                b1 += lr * (t - zin1)
                b2 += lr * (t - zin2)

    return (w11, w21, w12, w22, b1, b2, v1, v2, b3)


# XOR Data (Bipolar)
X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

T = np.array([-1, 1, 1, -1])

# Train the model
weights = madaline_xor(X, T, lr=0.5, epochs=5)


# Testing Phase
print("\nTesting the Madaline Network:")
for i in range(len(X)):
    x1, x2 = X[i]

    zin1 = weights[4] + x1*weights[0] + x2*weights[1]
    zin2 = weights[5] + x1*weights[2] + x2*weights[3]

    z1 = activation(zin1)
    z2 = activation(zin2)

    yin = weights[8] + z1*weights[6] + z2*weights[7]
    y = activation(yin)

    print(f"Input: {X[i]} → Output: {y}, Expected: {T[i]}")