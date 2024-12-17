while True:
    print("MENU\n1-Criar arquivo\n2-Mostrar arquivo\n3-Editar arquivo\n4-Sair do programa")
    
    
    try:
        num=int(input("\nDigite uma opcao:"))
    except ValueError:
        continue
    match num:
        case 1:
            nome=input("\nDigite o nome do arquivo:")
            with open (nome+".txt",'w') as file :
                x=input('\nDeseja adicionar escrita(sim ou nao)?')
                if x == 'sim':
                    file.write(input('\nDigite o que deseja adicionar ao arquivo:\n'))
                else :
                    pass
            
        case 2 :
            nome=input('\nQual o nome do arquivo?')
            try:
                with open (nome+'.txt','r')  as file:
                    conteudo=file.read()
                    print(conteudo)
            except Exception as e:
                with open ('gerenciamento_erros.log','a') as log :
                    log.write(f"\nErro ao abrir:{str(e)}\n")
                print('\nArquivo não existente')
                pass
            
        case 3 :
            try:
                num=int(input("\nQual opção desejada :\n 1-Abrir arquivo para reescrita \n 2-Adicionar escrita ao arquivo"))
            except ValueError:
                continue
            if num == 1 :
                
                try:
                    nome=input('\nQual o nome do arquivo?')
                    with open (nome+'.txt','w')  as file:
                        file.write(input('\nDigite o que deseja adicionar ao arquivo:\n'))

                except Exception as e:
                    with open ('gerenciamento_erros.log','a') as log :
                        log.write(f"\nErro ao abrir:{str(e)}\n")
                    print('\nArquivo não existente')
                    pass
                    
            if num == 2 :
                
                try:
                    nome=input('\nQual o nome do arquivo?')
                    with open (nome+'.txt','a')  as file:
                        
                        file.write(input('\nDigite o que deseja adicionar ao arquivo:\n'))

                except Exception as e:
                    with open ('gerenciamento_erros.log','a') as log :
                        log.write(f"\nErro ao abrir:{str(e)}\n")
                    print('\nArquivo não existente')
                    pass
        case 4 :
            print('Saindo do programa')
            break
                
            
            
            
            
            
                           
                    
                
