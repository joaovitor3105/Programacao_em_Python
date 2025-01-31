import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
temperatures = np.random.randint(20, 40, 30 * 3)

date_range = pd.date_range(start='2023-01-01', periods=30 * 3, freq='8H')

df = pd.DataFrame({'Date': date_range, 'Temperature': temperatures})

print(df)

df.plot(x='Date', y='Temperature', title='Temperature variation', grid=True,marker='o')
plt.show()