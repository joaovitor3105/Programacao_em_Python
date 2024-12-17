agenda=[[],[],[],[]]
x=1
menu=0

while(1):
    print('---------------------------------------')
    print('1-adicionar contato')
    print('2-remover contato')
    print('3-pesquisar contato')
    print('4-listar contatos')
    print('---------------------------------------')
    menu = int(input("Escolha uma opção: ")) 

    match menu:
        case 1:
            nome = input('Adicione o nome: ')
            agenda[0].append(nome)

           
            print('Adicione a data de nascimento:')
            dia = input('Dia: ')
            mes = input('Mês: ')
            ano = input('Ano: ')
            agenda[1].append(f'{dia}/{mes}/{ano}') 
            
            endereco = input('Adicione o endereço: ')
            agenda[2].append(endereco)

           
            telefone = input('Adicione o telefone: ')
            agenda[3].append(telefone)
        
        
        case 2:
            print('Qual contato deseja remover?')
            j = 0
            for i in agenda[0]:
                print(f'{j} - {i}') 
                j += 1

            num = int(input("Escolha o número do contato a remover: "))
            if 0 <= num < len(agenda[0]):
                for i in range(4):
                    del agenda[i][num]  
                print('Contato removido com sucesso!')
            else:
                print('Índice inválido.')


        case 3:
            print('Digite um contato para buscar:')
            nome = input()  
            encontrou = False
            for i in range(len(agenda[0])):
                if agenda[0][i] == nome:
                    print(f'Nome: {agenda[0][i]}')
                    print(f'Data de Nascimento: {agenda[1][i]}')
                    print(f'Endereço: {agenda[2][i]}')
                    print(f'Telefone: {agenda[3][i]}')
                    encontrou = True
                    break

            if not encontrou:
                print('Contato não encontrado.')
        case 4:
             if len(agenda[0]) == 0:
                print('Não há contatos na agenda.')
             else:
                for i in range(len(agenda[0])):
                    print(f'Nome: {agenda[0][i]}')
                    print(f'Data de Nascimento: {agenda[1][i]}')
                    print(f'Endereço: {agenda[2][i]}')
                    print(f'Telefone: {agenda[3][i]}')
                    print('---------------------------------------')
            
        


