import numpy as np
x=np.arange(-10,10,1)

noise=np.random.randn(20)

y=2*(x**3)+4*x+3+noise

x=x.reshape(len(x),1)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=3,include_bias=False)#equation ake maximum balaya danawa degree akata
#max power needed for x a0 is an 
#


xnew=poly.fit_transform(x)

model=LinearRegression()

model.fit(xnew,y)

#model.fit(x,y)

print('m: ',model.coef_)
print('c: ',model.intercept_)

#m=model.coef_
#c=model.intercept_

#y_best=m*x+c

from matplotlib import pyplot as plt

#plt.plot(x,y_best,'r')
plt.scatter(x,y)

plt.show()
