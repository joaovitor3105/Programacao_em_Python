
def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade: "))
        preco = int(input("Digite o preço : R$ "))
        if quantidade < 0 or preco < 0:
            print("Quantidade e preço devem ser positivos!")
            return
        estoque[nome] = {"quantidade": quantidade, "preco": preco}
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Por favor, digite números válidos")

def atualizar_quantidade(estoque):
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        try:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            if nova_quantidade < 0:
                print("A quantidade deve ser positiva")
                return
            estoque[nome]["quantidade"] = nova_quantidade
            print("Quantidade do produto atualizada com sucesso!")
        except ValueError:
            print("Por favor, digite um número válido")
    else:
        print("Produto não encontrado")

def remover_produto(estoque):
    nome = input("Digite o nome do produto a ser removido: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso")
    else:
        print("Produto não encontrado")

def exibir_relatorio(estoque):
    if not estoque:
        print("Estoque vazio!")
        return
        
    print("\nRELATÓRIO DE ESTOQUE")
    valor_total = 0
    
    for nome, info in estoque.items():
        quantidade = info["quantidade"]
        preco = info["preco"]
        total_produto = quantidade * preco
        valor_total += total_produto
        
        print(f"Produto: {nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço: R${preco:.2f}")
        print(f"Total: R${total_produto:.2f}")
        print("-----------------")
    
    print(f"Valor total do estoque: R${valor_total:.2f}")
    
def main():
    estoque = {}
    while True:
        print("\n SISTEMA DE GERENCIAMENTO DE ESTOQUE ")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Remover produto")
        print("4. Exibir relatório")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            atualizar_quantidade(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            exibir_relatorio(estoque)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")


main()