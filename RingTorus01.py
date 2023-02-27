import numpy as np
import matplotlib.pyplot as plt

figura=plt.figure(facecolor="Black")
ax=plt.axes(projection="3d")
plt.axis("off")
ax.set_facecolor("White")

angle=np.linspace(0,2*np.pi,30)
r,R=0.4,1.0
theta,phi=np.meshgrid(angle,angle)
X=(R+r*np.cos(phi))*np.cos(theta)
Y=(R+r*np.cos(phi))*np.sin(theta)
Z=r*np.sin(phi)

ax.set_xlim3d(-1,1)
ax.set_ylim3d(-1,1)
ax.set_zlim3d(-1,1)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='Blue')

plt.show()
