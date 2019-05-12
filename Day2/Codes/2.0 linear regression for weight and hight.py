import numpy as np
from matplotlib import pyplot as plt


train_data=[72,70,75,62,55,58,65,45,55,60,55,76,77,55,105,74,82,90,66,63,73,61,59,50,60,80,70,60,47]

train_target=[177,171,168,162,160,162,168,148,160,170,152,171,179,151,162,153,165,180,165,167,176,182,160,160,180,155,176,163,162]

#print(len(train_data))
#print(len(train_target))

train_data=np.array(train_data)

train_target=np.array(train_target)

train_data=train_data.reshape((len(train_data),1))#new function reshape-convert karanawa 2d array akak widihata rows 29k tina column 1k tina
#requirement in sklearn.train_data shoud be a 2D array
#print(train_data)

from sklearn.linear_model import LinearRegression#sklearn=si-kit learn

algo=LinearRegression()

algo.fit(train_data,train_target)#training the ml algorithem

test_data=[[84]]#data aka yawanawa algo akata dena

result=algo.predict(test_data)

print(result)

from matplotlib import pyplot as plt

plt.scatter(train_data,train_target)
plt.show()
