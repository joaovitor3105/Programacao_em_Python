amigos=["Libanes","Big alvaras","Jhon ","Bernas","Samu"]
retirado=amigos.pop(-1)
amigos.append("Jesus")
for i in amigos:
    print("Bora jantar guys:{}".format(i))
print("-----------------------------------------------------------------")
print ("O {}".format(retirado)+" não vai vim ")

print("-----------------------------------------------------------------")
for i in amigos:
    print("Bora jantar guys:{}".format(i))
print("-----------------------------------------------------------------")
amigos.append("Ben 10")
amigos.append("Temaki")
amigos.append("Yudi")
for i in amigos:
    print("Bora jantar guys:{}".format(i))
print("-----------------------------------------------------------------")
print(amigos[:])
print("-----------------------------------------------------------------")

ordenada=sorted(amigos)
print(ordenada)

print("-----------------------------------------------------------------")
for i in amigos:
    print("Amigos ordenados : {}".format(i))

print("-----------------------------------------------------------------") 

print("Reverso : {}".format(amigos.reverse()))

print("-----------------------------------------------------------------")

retangulo= (10,40)
print ("tupla:{}".format(retangulo))

retangulo=(12,50)
print ("tupla reformulada:{}".format(retangulo))