car=[]
opcionais={}
def make_car(modelo,fabricante,**adicionais):
    return {"Fabricante":fabricante,"Modelo":modelo,**adicionais}


fabricante=input("coloque o fabricante: ")
modelo=input("coloque o Modelo: ")

while True:
    chave=input("qual o opcinal ou digite sair: ")
    if chave=="sair":
        break
    valor=input(f"digite o opcional para {chave}:  ")
    opcionais[chave]=valor
    car=make_car(modelo,fabricante,**opcionais)
print (car)