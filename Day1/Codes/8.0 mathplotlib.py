from matplotlib import pyplot as plt#3 pyplot use to ploting
import numpy as np

x=np.arange(0,100,2)##0 sita 100 dakwa 2n dekara count wena array akak hedenawwa

y1=2*x
y2=x*x

plt.plot(x,y1)##plt=pyplot and x,y atara plot aka adinawa
plt.plot(x,y2)

plt.plot(x,y1,'r')##red colour aken
plt.plot(x,y2,'g')##green

plt.plot(x,y1,'r+')##first is colour 2nd is line type then + is line type
plt.plot(x,y2,'g.')

plt.show()##display plot



