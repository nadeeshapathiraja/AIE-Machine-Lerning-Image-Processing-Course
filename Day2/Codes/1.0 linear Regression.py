import numpy as np
x=np.arange(0,2000,1)
#y=2*x+3

noise=(np.random.rand(2000))
yn=2*x+3+noise
#yn=2*x+3+(np.random.rand(1)*2)#Display One random numbre

'''print(x)
print(y)
print(yn)'''

from sklearn.linear_model import LinearRegression

x=x.reshape(len(x),1)

model=LinearRegression()

model.fit(x,yn)

print('m ',model.coef_)
print('C ',model.intercept_)

'''

from matplotlib import pyplot as plt

plt.plot(x,y,'r')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(x,yn)

plt.show()'''


