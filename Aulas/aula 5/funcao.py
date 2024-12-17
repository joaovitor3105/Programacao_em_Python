def msg(nome,ID=0):
    """Exibe uma saudacao simples"""
    print(f"Ola como vai {nome}{ID}?")

def media(a=0,b=0,c=0):
    soma=0
    media=0
    num=0
    if a!= 0:
        soma+=a
        num+=1
    if b!= 0:
        soma+=b
        num+=1
    if c!= 0:
        soma+=c
        num+=1
    media=soma/num    
    return media
    
def mediainf(*num):
    soma=sum(num)
    nums=len(num)
    media=soma/nums 
    return media

def ordena(lst):
    lista=lst
    lista.sort()
    return lista
    
    
msg("BlueCold")
print(media(5,10))
print(mediainf(5,4,5,4,5,7,8,9,1,2,3,4))
lst=[5,4,3,2,1,0,7,9,6,4]
print(ordena(lst))
print(ordena(lst[:]))