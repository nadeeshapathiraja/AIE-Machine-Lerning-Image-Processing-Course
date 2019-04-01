import numpy as np

a= np.array(([1,2,3],[4,5,6]))
#print(a)

#print(a.shape)

#b=np.zeros((5,2),dtype=np.int)
b=np.ones((5,2),dtype=np.int)
#print(b)

c=np.random.randint(0,10,(2,3))
d=np.random.randint(0,10,(3,2))

print(c)
print(d)

z=np.matmul(c,d)
print(z)
