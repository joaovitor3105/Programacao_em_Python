import scipy.integrate  as spy
def f(x):
    return x**2
resultado, erro = spy.quad( f, 0, 2)
print(resultado)
print(erro)
