from random import randint


num=[]
for i in range(20) :
    numeros=randint(0,80)
    num.append(numeros)
    

print(num) 
print(max(num))
print(  min(num))
print(max(num)-min(num))
