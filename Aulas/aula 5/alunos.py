alunos={}
lst=[]


   



def make_aluno():
    while True:
        chave= input("Coloque o nome do aluno(ou sair): ")
        if(chave=="sair"):
            break
        value=input("coloque a nota:  ")
        alunos[chave]=value
        lst.append(alunos)
        return lst



print(make_aluno())