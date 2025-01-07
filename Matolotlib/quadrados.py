import matplotlib.pyplot as plt
plt.title('Quadrados',fontsize=24)
xdata = list(range(1,1001))
ydata = [x**2 for x in xdata]
plt.scatter(xdata,ydata,s=100,c=ydata,cmap=plt.cm.Blues)


plt.show()

