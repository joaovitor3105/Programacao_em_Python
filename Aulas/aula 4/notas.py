notas = {}

import random

notas['JP']= random.randint(1,10)
notas['Big Alvaras']= random.randint(1,10)
notas['Libas']= random.randint(1,10)
notas['Bernas']= random.randint(1,10)
notas['BlueCold']= random.randint(1,10)
media=0
for i in notas.values():
    media+=i

media=media/5
print (notas)

print(media)
if(media < 6):
    print('Rever a metodologia')


if(media == 6):
    print('Por pouco')

if(media > 6 ):
    print("Ai sim ")
