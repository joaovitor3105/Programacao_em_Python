from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
#Decaimento exponencial
def f(t, A, k, c):
    return A * np.exp(-k * t) + c

#Gerando os dados
t = np.linspace(0, 10, 50)
A = 5
k = 0.8
C = 1
y = f(t, A, k, C)
sigma = 0.5
noise = np.random.normal(0, sigma, t.shape)
y_noisy = y + noise
parametros, covariancia = curve_fit(f, t, y_noisy)
A_est, k_est, C_est = parametros

#Calculo do erro
error_A = abs(A_est - A)
error_k = abs(k_est - k)
error_C = abs(C_est - C)

#Printando  dados
print(f"\n\n\nParâmetros estimados: A = {A_est}, k = {k_est}, C = {C_est}")
print(f"Erro absoluto médio: A = {error_A}, k = {error_k}, C = {error_C}")

#Plotando os dados
plt.scatter(t, y_noisy, label='Dados experimentais (ruidosos)', color='blue')
t_fit = np.linspace(0, 10, 50)
y_fit = f(t_fit, A_est, k_est, C_est)
plt.plot(t_fit, y_fit, label='Ajuste de curva', color='red')
plt.plot(t_fit, f(t_fit, A, k, C), label='Curva real', color='green', linestyle='dashed')
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.legend()    
plt.show()
