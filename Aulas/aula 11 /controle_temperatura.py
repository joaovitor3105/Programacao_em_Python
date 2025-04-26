import pandas as pd
import matplotlib.pyplot as plt

a=[45,47,49,50,46,48,47]
b=[40,41,42,40,43,44,42]
c=[55,54,56,57,56,55,54]

df = pd.DataFrame({"A": a, "B": b, "C": c},
index = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"])
print(df)

print(df.loc[["Terça-feira","Quinta-feira"], "A"])
print(df>50)

df.plot(marker = "o", title = "Temperatura ao longo da semana", grid = True)
plt.show()