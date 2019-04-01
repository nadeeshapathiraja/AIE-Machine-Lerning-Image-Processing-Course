from matplotlib import pyplot as plt
import munpy as np

x=np.arange(0,2*np.pi,0.2)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,'r--',lable='sin(x)')
plt.plot(x,y2,'g+',lable='cos(x)')

plt.xlable('x valus (rads)')##lable x axis 
plt.ylable('sin(x) and cos(x)')##lable y axis

plt.title('Sin(X) and Cos(X)')##add title for plot

plt.savefig('mygraph.png')

plt.legend()##-- walin sin(x) + walin cos(x) kiyala pennananwa

plt.show()

