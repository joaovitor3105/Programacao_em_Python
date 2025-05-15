import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dados experimentais
comprimento = np.array([0.3, 0.6, 0.9, 1.21, 1.5, 1.6, 2.1, 2.4, 2.7, 2.99])
periodo = np.array([1.1, 1.6, 1.9, 2.3, 2.5, 2.7, 2.8, 3.1, 3.3, 3.5])

# Função para ajuste: y = A * x^(1/2)
def func(x, A):
    return A * np.sqrt(x)

# Realizando o ajuste da curva
params, params_covariance = curve_fit(func, comprimento, periodo)

# Obtendo o valor de A
A = params[0]
print(f"Valor de A encontrado no ajuste: {A:.4f}")

# Criando pontos para a curva de ajuste
x_fit = np.linspace(0, 3.2, 100)
y_fit = func(x_fit, A)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(comprimento, periodo, color='blue', label='Dados Experimentais')
plt.plot(x_fit, y_fit, 'r-', label=f'Ajuste: y = {A:.4f}·x^(1/2)')

# Configurando o gráfico
plt.xlabel('Comprimento (unidades)')
plt.ylabel('Período (unidades)')
plt.title('Gráfico de Período vs Comprimento com Ajuste y = A·x^(1/2)')
plt.grid(True)
plt.legend()

# Calculando o coeficiente de determinação (R²)
residuals = periodo - func(comprimento, A)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((periodo - np.mean(periodo))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"Coeficiente de determinação (R²): {r_squared:.4f}")

# Adicionar o valor de R² ao gráfico
plt.text(0.5, 3.3, f'R² = {r_squared:.4f}', fontsize=12)

plt.show()
