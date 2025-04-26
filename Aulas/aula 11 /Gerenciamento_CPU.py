import pandas as pd
import matplotlib.pyplot as plt

maquina1=[45,50,48,47]
maquina2=[55,53,58,56]
maquina3=[40,42,43,41]
maquina4=[70,75,72,73]
maquina5=[60,65,68,67]
data = data = pd.DataFrame({"Maquina 1": maquina1, "Maquina 2": maquina2, "Maquina 3": maquina3, "Maquina 4": maquina4, "Maquina 5": maquina5}, index = ["10;00", "14:00", "18:00", "22:00"])

print("Máquina 3 às 22:00:", data.loc["22:00", "Maquina 3"])
print(data)


data.plot(marker = "o", title = "Gerenciamento de CPU", grid = True)
plt.show()  