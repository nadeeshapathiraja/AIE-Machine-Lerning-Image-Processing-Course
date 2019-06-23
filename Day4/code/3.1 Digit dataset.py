from sklearn import datasets

digits=datasets.load_digits()

data=digits.data
target=digits.target

print(data.shape)#(number of images, size)
print(target.shape)

img= digits.images

from matplotlib import pyplot as plt

plt.imshow(img[0],cmap='binary')
plt.show()

#print(data[0])
#print(target[0])
