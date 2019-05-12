from sklearn import datasets#sklearn=sykitlearn library

iris=datasets.load_iris()#lording iris flower dataset into iris

data=iris.data#iris flower data , 150*4 array will be lorded to data
target=iris.target#iris flower target , 150*1 array will be lorded to data

#print(data)
#print(target)
#features=iris.feature_names
#print(features)

from sklearn.model_selection import train_test_split
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

                                                                                                                  
#print(test_target)

from sklearn.neighbors import KNeighborsClassifier #load KNN classifire

clsfr= KNeighborsClassifier(n_neighbors=3)# create object clsfr and use n_neighbors value for K

clsfr.fit(train_data,train_target)#use fit for tarin machine
#train_data(135*4)
#train_target(135*1)
#test_data(15*4)
#test_target(15*1)

result=clsfr.predict(test_data)

print("Predicted: ", result)
print("Actual: ",test_target)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(test_target,result)

print("Accuracy: ",accuracy)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #Axes3D used for 3 axes graphs


fig = plt.figure() #initialize the 3d graph

ax=fig.add_subplot(111,projection='3d')#adding 3axes to the fig graph 111-xyz

for i in range (0,len(train_target)):
    
    if(train_target[i]==0):#target is setosa
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],c='g')

    if(train_target[i]==1):#taget is verginica
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],c='r')

    if(train_target[i]==2):#target id versicolor
        ax.scatter(train_data[i][0],train_data[i][1],train_data[i][2],c='b')

print(result[0],test_target[0])

ax.scatter(test_data[0][0],test_data[0][1],test_data[0][2], c= 'c', marker='x')


plt.show()
























