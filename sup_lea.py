import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = [[1000], [1200], [1500], [1800], [2000]]
y = [10, 12, 15, 18, 20]

model = LinearRegression()
model.fit(X, y)
new_x = [[2200], [3000], [1150]]
pred = model.predict(new_x)

print(pred)
all = X + new_x

plt.scatter(X, y, label="Training Data")
plt.plot(all, model.predict(all), label="Regression Line")
plt.scatter(new_x, pred, marker="X", s=50, label="Predictions")
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("Linear Regression Visualization")
plt.legend()
plt.show()