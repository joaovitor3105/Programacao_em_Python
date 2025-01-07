import matplotlib.pyplot as plt

dados = [1,3,9,10,22,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
plt.title('Gráfico de Linha')
plt.plot(dados,linewidth=5)
plt.plot(dados)
plt.grid()
plt.xlabel('Obs',fontsize=14)
plt.ylabel('Dados',fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()
