import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

roteadores = {
    "Roteador1":{'media':10,'desvio':2},
    'Roteador2':{'media':15,'desvio':3},
    'Roteador3':{'media':20,'desvio':4},
    'Roteador4':{'media':25,'desvio':5},
}
medicoes = 100
dados = {}
#Dados de latência para os 4 roteadores usando NumPy

for roteador,parametros in roteadores.items():
    dados[roteador]=np.random.normal(
        loc = parametros['media'],
        scale = parametros['desvio'],
        size = medicoes)
    
#DataFrame com os dados simulados
    
df = pd.DataFrame(dados)
estatisticas = df.describe()

#Boxplot para comparar a latência dos roteadores

plt.subplot(2, 1, 1)
sns.boxplot(data=df)
plt.title('Distribuição de Latência por Roteador')
plt.ylabel('Latência (ms)')

#Porcentagem de medições com latência acima de 18 ms para cada roteador

porcentagens_acima_18ms = {}
for roteador in roteadores.keys():
    acima_18ms = (df[roteador] > 18).sum()
    porcentagem = (acima_18ms / medicoes) * 100
    porcentagens_acima_18ms[roteador] = porcentagem
for router, porcentagem in porcentagens_acima_18ms.items():
    print(f"{router}: {porcentagem:.2f}%")


#plotando historiograma

plt.subplot(2, 1, 2)
for roteador in roteadores.keys():
    sns.histplot(data=df[roteador], label=roteador, alpha=0.5, bins=20)
plt.title('Histograma de Latência por Roteador')
plt.xlabel('Latência (ms)')
plt.ylabel('Contagem')
plt.legend()
plt.tight_layout()
plt.show()
