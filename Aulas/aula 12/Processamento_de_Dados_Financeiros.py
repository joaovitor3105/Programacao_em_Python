import random

# Tamanho do tabuleiro
TAMANHO_TABULEIRO = 10

# Número de embarcações
NUM_EMBARCAÇÕES = 5

# Símbolos para representar o tabuleiro
AGUA = '~'
EMBARCAÇÃO = 'N'
TIRO_AGUA = 'O'
TIRO_EMBARCAÇÃO = 'X'

# Função para criar um tabuleiro vazio
def criar_tabuleiro():
    return [[AGUA for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro, revelar_embarcações=False):
    print("  " + " ".join(str(i) for i in range(TAMANHO_TABULEIRO)))
    for i, linha in enumerate(tabuleiro):
        if revelar_embarcações:
            print(i, " ".join(linha))
        else:
            print(i, " ".join([AGUA if celula == EMBARCAÇÃO else celula for celula in linha]))

# Função para posicionar as embarcações
def posicionar_embarcações(tabuleiro):
    embarcações_posicionadas = 0
    while embarcações_posicionadas < NUM_EMBARCAÇÕES:
        x = random.randint(0, TAMANHO_TABULEIRO - 1)
        y = random.randint(0, TAMANHO_TABULEIRO - 1)
        if tabuleiro[x][y] == AGUA:
            tabuleiro[x][y] = EMBARCAÇÃO
            embarcações_posicionadas += 1

# Função para realizar um tiro
def realizar_tiro(tabuleiro, x, y):
    if tabuleiro[x][y] == EMBARCAÇÃO:
        tabuleiro[x][y] = TIRO_EMBARCAÇÃO
        return True
    elif tabuleiro[x][y] == AGUA:
        tabuleiro[x][y] = TIRO_AGUA
        return False
    else:
        return False

# Função para verificar se todas as embarcações foram afundadas
def todas_embarcações_afundadas(tabuleiro):
    for linha in tabuleiro:
        if EMBARCAÇÃO in linha:
            return False
    return True

# Função principal do jogo
def jogar_batalha_naval():
    # Inicialização dos tabuleiros
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()

    # Posicionamento das embarcações
    posicionar_embarcações(tabuleiro_jogador)
    posicionar_embarcações(tabuleiro_computador)

    # Loop principal do jogo
    while True:
        print("\nSeu tabuleiro:")
        exibir_tabuleiro(tabuleiro_jogador, revelar_embarcações=True)
        print("\nTabuleiro do computador:")
        exibir_tabuleiro(tabuleiro_computador)

        # Vez do jogador
        while True:
            try:
                x = int(input("Digite a linha para atirar: "))
                y = int(input("Digite a coluna para atirar: "))
                if 0 <= x < TAMANHO_TABULEIRO and 0 <= y < TAMANHO_TABULEIRO:
                    break
                else:
                    print("Coordenadas fora do tabuleiro. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite números inteiros.")

        acertou = realizar_tiro(tabuleiro_computador, x, y)
        if acertou:
            print("Você acertou uma embarcação!")
            if todas_embarcações_afundadas(tabuleiro_computador):
                print("Parabéns! Você afundou todas as embarcações do computador!")
                break
        else:
            print("Você atingiu a água.")
            

        # Vez do computador
        print("\nVez do computador...")
        while True:
            x = random.randint(0, TAMANHO_TABULEIRO - 1)
            y = random.randint(0, TAMANHO_TABULEIRO - 1)
            if tabuleiro_jogador[x][y] not in [TIRO_AGUA, TIRO_EMBARCAÇÃO]:
                break

        acertou = realizar_tiro(tabuleiro_jogador, x, y)
        if acertou:
            print(f"O computador acertou uma embarcação na posição ({x}, {y})!")
            if todas_embarcações_afundadas(tabuleiro_jogador):
                print("O computador afundou todas as suas embarcações! Você perdeu.")
                break
        else:
            print(f"O computador atingiu a água na posição ({x}, {y}).")

# Iniciar o jogo
jogar_batalha_naval()