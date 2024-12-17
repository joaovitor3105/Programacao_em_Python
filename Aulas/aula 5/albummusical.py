
lst=[]
dic={}


def make_album(titulo,artista):
    dic={"artista":artista,"titulo":titulo}
    lst.append(dic)
    


while True:
    titulo=input("Insira o titulo:")
   
    artista=input("Insira o artista:")
    
    make_album(titulo,artista)
    print(lst)
