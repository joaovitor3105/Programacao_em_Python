import pandas as pd
import numpy as np


np.random.seed(0)
temperatures = np.random.randint(20, 30,168)
pressao = np.random.randint(1,5,168)
vib=np.random.randint(1,100,168)
hora= np.arange(1,169)

df = pd.DataFrame({"Hora": hora,"Temperatura": temperatures, "Pressão": pressao, "Vibração": vib })
df_sorted = df.sort_values(by="Vibração", ascending=False)
print(df_sorted)
df_sorted.to_excel("Analise_Dados.xlsx", index=False)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df['Hora'], df['Temperatura'], label='Temperatura')
plt.plot(df['Hora'], df['Pressão'], label='Pressão')
plt.plot(df['Hora'], df['Vibração'], label='Vibração')
plt.xlabel('Hora')
plt.ylabel('Valores')
plt.title('Análise de Dados')
plt.legend()
plt.grid(True)
plt.savefig('Analise_Dados.png')
plt.show()