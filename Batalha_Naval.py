# Jogo de batalha naval
import random

# Definição de cores para o terminal
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
ROXO = "\033[95m"
RESET = "\033[0m"  

# Função para criar o tabuleiro do jogo
def criar_tabuleiro():
    # Cria uma matriz 10x10 preenchida com "~" que representa água
    matriz = [["~" for _ in range(10)] for _ in range(10)]
    return matriz

# Função para posicionar embarcações aleatoriamente no tabuleiro
def posicionar_embarcacoes_aleatorias(tabuleiro):
    embarcacoes = 0
    # Posiciona 5 embarcações aleatoriamente no tabuleiro
    while embarcacoes < 5:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Verifica se a posição está vazia
        if tabuleiro[x][y] == "~":
            tabuleiro[x][y] = "["
            embarcacoes += 1

# Função para o jogador posicionar suas embarcações manualmente
def posicionar_embarcacao(tabuleiro):
    embarcacoes = 0
    # Permite ao jogador posicionar 5 embarcações
    while embarcacoes < 5:
        print(f"{AMARELO}Digite as posições para adicionar a embarcação:{RESET}")
        mostrar_tabuleiro_revelado(tabuleiro)
        try:
            x = int(input("Digite a linha: ")) 
            y = int(input("Digite a coluna: "))

            # Verifica se a posição é válida
            if (x < 0 or x > 9 or y < 0 or y > 9):
                print(f"{VERMELHO}Posição inválida, tente novamente.{RESET}")
                continue
            # Verifica se a posição está vazia
            if tabuleiro[x][y] == "~":
                tabuleiro[x][y] = "["
                embarcacoes += 1
                print(f"{VERDE}Embarcação adicionada!{RESET}")
            else:
                print(f"{VERMELHO}Posição já ocupada, tente outra.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Digite um valor inteiro{RESET}")
            continue

# Função para o computador realizar um tiro
def tiro_computador(tabuleiro):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Verifica se a posição já foi atacada
        if tabuleiro[x][y] == "X" or tabuleiro[x][y] == "*":
            continue
        else:
            break
    # Verifica se acertou uma embarcação
    if tabuleiro[x][y] == "[":
        tabuleiro[x][y] = "X"
        return True
    else:
        tabuleiro[x][y] = "*"
        return False

# Função para o jogador realizar um tiro
def tiro_jogador(tabuleiro):
    print(f"{AMARELO}\nFaça um tiro!\n{RESET}")
    while True:
        try:
            x = int(input("\nDigite a linha: ")) 
            y = int(input("\nDigite a coluna: "))
            # Opção para revelar o tabuleiro do computador
            if x == 100 or y == 100:
                print("\nTabuleiro do Computador Revelado:")
                mostrar_tabuleiro_revelado(tabuleiro)
                continue

            # Verifica se a posição é válida
            elif (x < 0 or x > 9 or y < 0 or y > 9):
                print(f"{VERMELHO}Posição inválida, tente novamente.{RESET}")
                continue
            # Verifica se a posição já foi atacada
            if tabuleiro[x][y] == "X" or tabuleiro[x][y] == "*":
                print(f"{VERMELHO}Posição já atirada, tente outra.{RESET}")
                continue
            else:
                break
        except ValueError:
            print(f"{VERMELHO}Digite um valor inteiro{RESET}")
            continue

    # Verifica se acertou uma embarcação
    if tabuleiro[x][y] == "[":
        tabuleiro[x][y] = "X"
        return True
    else:
        tabuleiro[x][y] = "*"
        return False

# Função para mostrar o tabuleiro oculto (sem revelar as embarcações)
def mostrar_tabuleiro_oculto(tabuleiro):
    print("  ", end="")
    for i in range(10):
        print(i, end=" ")
    print()
    for idx, i in enumerate(tabuleiro):
        print(idx, end=" ")
        for j in i:
            if j == "[" or j == "~":
                print("-", end=" ")
            else:
                print(j, end=" ")
        print()
    print("\n")

# Função para mostrar o tabuleiro revelado (com as embarcações)
def mostrar_tabuleiro_revelado(tabuleiro):
    print("  ", end="")
    for i in range(10):
        print(i, end=" ")
    print()
    for idx, i in enumerate(tabuleiro):
        print(idx, end=" ")
        for j in i:
            print(j, end=" ")
        print()
    print("\n")

# Função principal para iniciar o jogo
def iniciar_jogo():
    acertos_jogador = 0
    acertos_computador = 0

    # Iniciando jogo para usuário
    print(f"\n{ROXO}=== BATALHA NAVAL ==={RESET}")
    print(f"{AMARELO}Prepare-se para a batalha!\n{RESET}")
    
    # Criando tabuleiros para o jogador e o computador
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    
    # Posicionando embarcações no tabuleiro do computador aleatoriamente
    print(f"{AMARELO}Primeiro, vamos posicionar seus navios!{RESET}")
    posicionar_embarcacoes_aleatorias(tabuleiro_computador)
    
    # Permite ao jogador posicionar suas embarcações manualmente
    posicionar_embarcacao(tabuleiro_jogador)
    
    # Looping principal do jogo
    while True:
        # Turno do jogador
        print(f"\n{AMARELO}{'='*40}{RESET}")
        print(f"{AMARELO}=== SEU TABULEIRO ==={RESET}")
        mostrar_tabuleiro_revelado(tabuleiro_jogador)
        print(f"{AMARELO}\n=== SUA VEZ DE JOGAR ==={RESET}")
        print(f"{AMARELO}Seus acertos: {acertos_jogador}/5{RESET}")
        
        # Jogador realiza um tiro
        while True:
            print("\nTabuleiro do computador:\n")
            mostrar_tabuleiro_oculto(tabuleiro_computador)
            verificacao = tiro_jogador(tabuleiro_computador)
            if verificacao: 
                acertos_jogador += 1
                print(f"{VERDE}\nExcelente tiro! Você tem {acertos_jogador} acertos de 5 necessários.{RESET}")

                # Verifica se o jogador venceu
                if acertos_jogador == 5:
                    print(f"\n{ROXO}🎉 PARABÉNS! Você venceu o jogo! 🎉{RESET}")
                    exit()
                else:
                    print(f'{VERDE}\nVocê acertou! Ganhou mais um tiro!{RESET}')
                    continue
            else:
                print(f"{VERMELHO}\nVocê errou. Vez do computador...{RESET}") 
                break

        # Turno do computador
        print(f"\n{AMARELO}{'='*40}{RESET}")
        print(f"{AMARELO}=== VEZ DO COMPUTADOR ==={RESET}")
        print(f"{AMARELO}Acertos do computador: {acertos_computador}/5{RESET}")        
        
        # Computador realiza um tiro
        while True:
            verificacao = tiro_computador(tabuleiro_jogador)
            if verificacao:
                acertos_computador += 1
                print(f"{VERMELHO}\nO computador acertou! ({acertos_computador}/5 acertos){RESET}")

                # Verifica se o computador venceu
                if acertos_computador == 5:
                    print(f"\n{AZUL}❌ Game Over! O computador venceu! ❌{RESET}")
                    exit()
                else:
                    print(f"{VERMELHO}\nO computador vai atirar novamente!{RESET}")
                    continue
            else:
                print(f"{VERDE}\nO computador errou! Sua vez de jogar...{RESET}")
                break  

# Inicia o jogo
iniciar_jogo()