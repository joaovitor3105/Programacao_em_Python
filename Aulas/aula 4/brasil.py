estado={}
brasil=[]

for c in range(3):
    estado["UF"]=str(input("unidade federativa:"))
    estado["Sigla"]=str(input("Sigla do estado:"))
    brasil.append(estado.copy())
print(brasil)