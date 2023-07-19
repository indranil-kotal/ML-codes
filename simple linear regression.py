import matplotlib.pyplot as plt
from scipy import stats
x=[40 , 50 , 60 , 70]
y=[6.2 , 7.2 , 9.1 , 12]
pre = float(input("Enter the independent variable value to predict y: "))
slope , intercept , r , p , std_err = stats.linregress(x , y)
def starLine(x):
 return slope * x + intercept
my_mod = list(map(starLine , x))
print('The predicted value at point ',pre,' is:',starLine(pre))
plt.title('Simple ploting')
plt.scatter(x,y)
plt.plot(x , my_mod)
plt.show()
