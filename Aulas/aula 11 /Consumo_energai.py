import pandas as pd
import matplotlib.pyplot as plt

data_norte = [2500,2700,3000,2800]
data_sul = [2300,2200,2400,2600]
data_leste = [3100,3200,3300,3400]

df = pd.DataFrame({"Norte": data_norte, "Sul": data_sul, "Leste": data_leste},index = [1,2,3,4])
print(df)

print(df[(df > 2500) & (df < 3500)])
data= df[(df > 2500) & (df < 3500)]

data.plot(marker = "o", title = "Consumo de energia ao longo do ano", grid = True)
plt.show()

