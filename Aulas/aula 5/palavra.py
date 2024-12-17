

def palavra():
    cont ={}
    palavra=input("digite a palavra:  ")
    for i in palavra:
        if i in cont:
            cont[i] += 1
        else:
            cont[i] = 1 
    return cont
    
print(palavra())