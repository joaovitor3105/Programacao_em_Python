carros=["ferrari","lamborguini","jaguar","mercedes ","lexus","corvete","chevrolet","ford","mustang","dodge"]
carros.append("madza")
carros.append("nissan")
carros.insert(0,"toyota")
carros.insert(-2,"porsche")

for i in range (len(carros)):
    print ("Gostaria de ter um {}".format(carros[i]))

  

retirado=carros.pop(0) 
print(retirado)

carros.remove("lexus")

for i in range (len(carros)):
    print ("Gostaria de ter um {}".format(carros[i]))


