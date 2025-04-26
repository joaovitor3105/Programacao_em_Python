cadastro={}




while True:
    menu=0
    menu=input("1-adicionar no dicionario \n 2-mostrar dicionario \n3-Sair")
    match menu:
            case 1:
            
                    cadastro ["CPF"]=input("Insira o cpf:")
                    cadastro ["ID"]=input("Insira o ID:")
                    cadastro ["CEP"]=input("Insira o cep:")
                    cadastro ["Cidade"]=input("Insira a cidade natal:")
                    cadastro ["Telefone"]=input("Insira o telefone:")
                    
            case 2:
                print(cadastro)

            case 3:
                exit
            