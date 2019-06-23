from sklearn.datasets import load_iris

iris=load_iris()

data=iris.data
target=iris.target

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target = train_test_split(data,target,test_size=0.2)


from sklearn.svm import SVC

clsfr=SVC()

clsfr.fit(train_data,train_target)
result=clsfr.predict(test_data)

#print(clsfr)
from sklearn.metrics import accuracy_score

accuracy= accuracy_score(test_target,result)
print("Accuracy : " ,accuracy)
