import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def get_user_input():
    n = int(input("Enter the number of data points: "))
    data = [list(map(float, input("Enter house size and price: ").split())) for _ in range(n)]
    return np.array(data)

user_data = get_user_input()
X, Y = user_data[:, 0].reshape(-1, 1), user_data[:, 1]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


model = LinearRegression().fit(X_train, Y_train)
Y_pred = model.predict(X_test)


print(f'Mean Squared Error: {mean_squared_error(Y_test, Y_pred):.2f}')
print("Predictions:")
for size, price in zip(X_test, Y_pred):
    print(f"House Size: {size[0]:.2f}, Predicted Price: {price:.2f}")





#for graph




import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def get_user_input():
    n = int(input("Enter the number of data points: "))
    return np.array([list(map(float, input("Enter house size and price: ").split())) for _ in range(n)])

user_data = get_user_input()
X, Y = user_data[:, 0].reshape(-1, 1), user_data[:, 1]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



model = LinearRegression().fit(X_train, Y_train)
Y_pred = model.predict(X_test)

print(f'Mean Squared Error: {mean_squared_error(Y_test, Y_pred):.2f}')
print("Predictions:")
for size, price in zip(X_test.flatten(), Y_pred):
    print(f"House Size: {size:.2f}, Predicted Price: {price:.2f}")

plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("House Size")
plt.ylabel("Price")
plt.title("Linear Regression - House Price Prediction")
plt.legend()
plt.show()