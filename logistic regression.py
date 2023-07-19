from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
x=np.array([[19,19000], [35,2000], [26,43000],[27,57000],[19,76000],
[27,58000],[27,84000], [32,150000],[25,33000],[35,65000], [26,80000],
[26,52000],[20,86000],[32,18000],[18,82000],[29,80000],[47,25000],[45,26000],
[46,28000]])
y=np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
model=linear_model.LogisticRegression()
p=float(input("enter first independent variable value: "))
q=float(input("enter second independent variable value: "))
model.fit(x_train,y_train)
pre=model.predict([[p,q]])
print("predicted value is ",int(pre))
