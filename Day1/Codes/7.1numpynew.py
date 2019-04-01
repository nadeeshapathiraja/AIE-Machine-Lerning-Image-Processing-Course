import numpy as np

array=np.random.randint(0,20,(5,10))

print(array)

print('===============================')
#print(array[1,:])##first coloum
#print(array[:,1])##firxt row 

#print(array[0:2,3:8])

print(sum(array))
print(np.sum(array))
print(np.sum(array,axis=1))##coloum by coloum sum
print(np.sum(array,axis=1))##row by row sum

print(np.sum(array[2:4,0:5]))
