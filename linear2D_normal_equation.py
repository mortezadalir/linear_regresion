

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(30,100,20)
y=4*x+50+np.random.normal(0,25,20)
colors='#1b3fe0'
area=np.pi*5
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot of train data')
plt.xlabel('x')
plt.ylabel('y')
oness=np.ones(20)
X_T= np.array([ oness, x])
X=np.matrix.transpose(X_T)
y_t=np.matrix.transpose(y)
XY1=np.dot(X_T,y_t)
teta=np.dot(np.linalg.inv(np.dot(X_T,X)),XY1)
x1=np.linspace(20,120,20)
y1=teta[1]*x1+teta[0]
colors1=('red')
plt.plot(x1,y1,c=colors1)
plt.show()
