import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
X_train = np.array([[1], [2], [3], [4], [5], [6], [7]])
Y_train = np.array([45000, 50000, 60000, 80000, 110000, 150000, 200000])
degree = 2 # Specify the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree)
X_poly_train = poly_features.fit_transform(X_train)
model = LinearRegression()
model.fit(X_poly_train, Y_train)
Y_pred_train = model.predict(X_poly_train)
mse = mean_squared_error(Y_train, Y_pred_train)
rmse = np.sqrt(mse)
r2 = r2_score(Y_train, Y_pred_train)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2) Score:", r2)
