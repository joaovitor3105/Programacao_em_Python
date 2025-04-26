import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

print(a)

b=np.zeros(2,dtype=np.int64)
print (b)

c= np.arange(0,100,2)
print(c)

a=np.array([1,2,3,4,5,6,7,8,9,10])

b=a[3:8]

b[0]=11
print (a)

