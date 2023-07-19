from sklearn import linear_model
import numpy as np
x = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
y = np.array([1, 2, 3, 4])
reg = linear_model.LinearRegression()
reg.fit(x, y)
p=float(input("enter first independent variable value: "))
q=float(input("enter second independent variable value: "))
r=float(input("enter third independent variable value: "))
pre=reg.predict([[p,q,r]])
print("predict value is", int(pre))
