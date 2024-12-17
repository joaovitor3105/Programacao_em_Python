pizzas=["calabresa","frango catupiry","4  queijos"]

for i in pizzas:
    print("A pizza de {}".format(i) + " e muito gostosa")

print("Eu amo muito pizza ")
print("-----------------------------------------------------------------")
animais=["cachorro","gato","cobra"]

for i in animais:
    if(i=="cachorro"):
        print("O {}".format(i) + " e divertido")
    if(i=="gato"):
        print("O {}".format(i) + " e fofo")
    if(i=="cobra"):
        print("A {}".format(i) + " rasteja pelo châo")

print("-----------------------------------------------------------------")

milhao=[]

for i in range(0,10000001,1):
    milhao.append(i)

print(min(milhao))
print(max(milhao))
print(sum(milhao))

print("-----------------------------------------------------------------")
impares=[]
for i in range(1,20,2):
    impares.append(i)
    

print(impares)

multiplos=[]

for i in range(3,31,3):
    multiplos.append(i)

print(multiplos)

for i in range(1,11,1):
    print(i**3)

print("-----------------------------------------------------------------")

