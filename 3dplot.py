import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
f=open("sample.txt",'r')
f1=f.readline()
f2=f.readlines()
t=[]
spl=[]
s=[]
for row in f2:
    t.append(float(row.split( )[1]))
    spl.append(float(row.split( )[2]))
    s.append(float(row.split( )[3]))
X=t
Y=spl
Z=s
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax=fig.gca(projection='3d')
ax.scatter(X,Y,Z,c='r',marker='x')
ax.set_xlabel(f1.split( )[0])
ax.set_ylabel(f1.split( )[1])
ax.set_zlabel(f1.split( )[2])
plt.show()
