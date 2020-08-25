
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
excel_file = 'grv1.xlsx'
df = pd.read_excel(excel_file)
XX=df.to_numpy()
print(XX)
colors='#1b3fe0'
oness=np.ones(25)
x=XX[:,0:2]
X_T= np.array([ oness ,x[:,0] ,x[:,1]])
#C = np.concatenate((oness, x))
#X_T=np.append(oness,x,2)
X=np.matrix.transpose(X_T)
y_t=np.matrix.transpose(XX[:,2])
XY1=np.dot(X_T,y_t)
teta=np.dot(np.linalg.inv(np.dot(X_T,X)),XY1)
x1=np.linspace(20,120,20)
y1=teta[1]*x1+teta[0]
colors1=('red')
plt.plot(x1,y1,c=colors1)
plt.show()
