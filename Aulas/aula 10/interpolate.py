import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt

tensao= np.array([0,1,2,3,4])
corrente = np.array([1.2,2.4,3.1,4.0,5.2])

f = spi.interp1d(tensao,corrente)
tensao_nova = np.linspace(0,4,100)
corrente_nova = f(tensao_nova)
plt.plot(tensao,corrente,'o',tensao_nova,corrente_nova)
plt.show()