from scipy.optimize import curve_fit
import numpy as np

temp= np.array([42,53,61,72,79,83,90,102,111,119])
hora = np.array([0,1,2,3,4,5,6,7,8,9])
def f(x,a,b):
    return a*x+b
parametros, covariancia = curve_fit(f,temp,hora)
print(parametros)
print(covariancia)

import matplotlib.pyplot as plt
plt.plot(temp,hora,'o')
plt.plot(temp,f(temp,*parametros))
plt.show()

