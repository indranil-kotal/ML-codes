import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,5*np.pi,0.1)
y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,color='green')
plt.plot(x,y2,color='darkblue')
plt.show()