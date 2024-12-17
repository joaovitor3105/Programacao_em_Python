with open ('arq.txt','r' ) as file:
    conteudo=file.read()
    for j in range(3):
        for i in conteudo:
           print (i,end='')
    print(conteudo.replace("python","java"))
    