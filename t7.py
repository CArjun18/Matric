# User input for dataset size
n = int(input("Enter the number of data points: "))
X = []
Y = []

print("Enter house sizes and corresponding prices:")
for _ in range(n):
    size, price = map(float, input().split())
    X.append(size)
    Y.append(price)

# Calculating mean values
X_mean = sum(X) / len(X)
Y_mean = sum(Y) / len(Y)

# Calculating slope (m) and intercept (b) for y = mx + b
numerator = sum((X[i] - X_mean) * (Y[i] - Y_mean) for i in range(n))
denominator = sum((X[i] - X_mean) ** 2 for i in range(n))
m = numerator / denominator
b = Y_mean - m * X_mean

# Predicting and displaying results
print("Predictions:")
for size in X:
    predicted_price = m * size + b
    print(f"House Size: {size:.2f}, Predicted Price: {predicted_price:.2f}")

# Calculating Mean Squared Error
mse = sum((Y[i] - (m * X[i] + b)) ** 2 for i in range(n)) / n
print(f'Mean Squared Error: {mse:.2f}')
