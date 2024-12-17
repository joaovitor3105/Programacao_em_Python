while True:
    nome=input("Digite um nome:")
    if nome =='q':
        break
    print(f"saudacoes {nome}!")
    with open ('guest_book.txt','a') as file :
        file.write(nome+'\n')
        
