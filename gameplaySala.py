import random
import time
import os

PORTA_AVIOES = "PORTA-AVIÕES 🚢"
NAVIO_TANQUE = "NAVIO-TANQUE 🚤"
CONTRATORPEDEIRO = "CONTRATORPEDEIRO ⛵️"
SUBMARINO = "SUBMARINO 🛶"
DESTROIER = "DESTROIER 🛀"
COMPUTADOR = "computador 🤖"
HUMANO = "jogador 🫵 "

# conversão de caractere para numero, coordenadas das linhas
def converter_caractere(caractere):
    if caractere == "a" or caractere == "1":
        return 1
    elif caractere == "b" or caractere == "2":
        return 2
    elif caractere == "c" or caractere == "3":
        return 3
    elif caractere == "d" or caractere == "4":
        return 4
    elif caractere == "e" or caractere == "5":
        return 5
    elif caractere == "f" or caractere == "6":
        return 6
    elif caractere == "g" or caractere == "7":
        return 7
    elif caractere == "h" or caractere == "8":
        return 8
    elif caractere == "i" or caractere == "9":
        return 9
    elif caractere == "j" or caractere == "10":
        return 10
    else:
        print("❌ Digite uma posição válida! \n")
        return -1

def converter_eixo(eixo):
    if eixo == "horizontal" or eixo == "x" or eixo == "h" or eixo == 0:
        return "x"
    elif eixo == "vertical" or eixo == "y" or eixo == "v" or eixo == 1:
        return "y"
    else:
        print("\n❌ Digite um valor válido!\n")
        return -1

def limpar_terminal():
    # 'nt' é para Windows, 'posix' é para macOS e Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_matriz(matriz):
    for i in range(0, len(matriz)):
        linha = matriz[i]
        print(" ".join(map(str, linha))) # JOIN MAP PRINTA A MATRIZ BONITINHO SEM VIRGULA NO MEIO
    print()

def criar_matriz_front():
    return [
    ['-',' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10'],
    ['A','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['B','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['C','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['D','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['E','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['F','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['G','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['H','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['I','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ['J','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊','🌊'],
    ]

def criar_matriz_back():
    return [
    # 0 #1 #2 #3 #4 #5 #6 #7 #8 #9 #10#11
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    ]


def input_coord():
    linha = -1
    coluna = -1

    while linha == -1:
        linha = input("Digite a LINHA (LETRA) da posição aqui: \n").strip().lower()
        linha = converter_caractere(linha)

    while coluna == -1:
        coluna = input("Digite a COLUNA (NUMERO) da posição aqui: \n").strip().lower()
        coluna = converter_caractere(coluna)

    return linha, coluna

def pegar_qtd_barcos(vidasBarcos, barcoAtingido):
    afundouBarco = False
    qtdBarcos = 0
    indice = barcoAtingido - 1 # IDs vão de 1 a 5, lista vai de 0 a 4. (ele converte o id dos barcos para o indice da lista)
    if 0 <= indice < len(vidasBarcos): # se o indice for 0,1,2,3,4, ele acessa a lista e tira uma vida do barco correspondente
        vidasBarcos[indice] -= 1
        if vidasBarcos[indice] == 0:
            afundouBarco = True

    for vida in vidasBarcos:
        if vida > 0:
            qtdBarcos += 1

    return qtdBarcos, vidasBarcos, afundouBarco

def adicionar_barco_matriz(matrizBack, matrizFront, linha, coluna, tamanho, direcao, jogador):
    repetir = True
    id = tamanho

    while repetir:
        podePosicionar = True

        linha, coluna = input_coord()

        limpar_terminal()

        if direcao == "x":
            for i in range(tamanho):
                if coluna > (12 - tamanho) or matrizBack[linha][coluna+i] != 0: # Se sair do tabuleiro ou colidir
                    podePosicionar = False

            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matrizBack[linha][coluna+i] = id
            else:
                print_matriz_convertida(matrizBack, matrizFront, "posicionando", jogador)
                print("❌ O seu barco está saindo do tabuleiro ou colidindo com outro barco! Escolha uma posição válida! \n")

        elif direcao == "y":
            for i in range(tamanho):
                if linha > (12 - tamanho) or matrizBack[linha+i][coluna] != 0: # Se sair do tabuleiro ou colidir
                    podePosicionar = False

            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matrizBack[linha+i][coluna] = id
            else:
                print_matriz_convertida(matrizBack, matrizFront, "posicionando", jogador)
                print("❌ O seu barco está saindo do tabuleiro ou colidindo com outro barco! Escolha uma posição válida!")

def verificar_acerto_tiro(matrizBack, matrizFront, linha, coluna):
    if matrizBack[linha][coluna] != 0 and matrizBack[linha][coluna] != -1 and matrizBack[linha][coluna] != 7 and matrizBack[linha][coluna] != 6: # Se acertou um barco
        barcoAtingido = matrizBack[linha][coluna] # Pega o ID do barco atingido
        matrizBack[linha][coluna] = 6 # Marca como atingido na matriz de dados
        matrizFront[linha][coluna] = '💥' # Atualiza o visual na matriz de exibição
        return barcoAtingido
    elif matrizBack[linha][coluna] == 0: # Se errou
        matrizBack[linha][coluna] = 7 # Marca como água atingida
        matrizFront[linha][coluna] = '🌀' # Atualiza o visual
        return None # Indica que foi um erro

def print_matriz_convertida(matrizBack, matrizFront, situacao, jogador):
    print(f"--- Tabuleiro do {jogador} ---\n")

    if situacao == "posicionando":
        simbolos = ["", "🛀", "🛶", "⛵️", "🚤", "🚢"] # Lista com os símbolos dos barcos
        for linha in range(1, 11):
            for coluna in range(1, 11):
                valor = matrizBack[linha][coluna] # Pega o valor da posição na matriz de dados
                if valor >= 1 and valor <= 5: # Se o valor for entre 1 e 5 (significa que é um barco)
                    matrizFront[linha][coluna] = simbolos[valor] # Põe na matriz de exibição o símbolo do barco

    elif situacao == "jogando":
        # Ao jogar, mantém os acertos/erros, mas esconde os barcos não atingidos
        for linha in range(1,11):
            for coluna in range(1,11):
                if matrizBack[linha][coluna] >= 1 and matrizBack[linha][coluna] <= 5: # Se a posição verificada for igual a um barco
                    # Mostra a onda original apenas se não foi atingido
                    if matrizFront[linha][coluna] != '💥':
                        matrizFront[linha][coluna] = "🌊"

    return print_matriz(matrizFront)

def posicionar_barco_jogador(barco, jogador, matrizFront, matrizBack):
    if barco == PORTA_AVIOES:
        tamanho = 5
    elif barco == NAVIO_TANQUE:
        tamanho = 4
    elif barco == CONTRATORPEDEIRO:
        tamanho = 3
    elif barco == SUBMARINO:
        tamanho = 2
    elif barco == DESTROIER:
        tamanho = 1
    else:
        print(f"ERRO! dev digitou barco inexistente! {barco}")
        return

    eixo = -1
    linha = -1
    coluna = -1

    print(f"👉 Agora {jogador} está posicionando o {barco}, de TAMANHO {tamanho}\n")

    if tamanho != 1: # Só entra aqui se o tamanho do barco NÃO for 1, não há por que escolher orientação de barco tamanho 1
        print("◽️ Escolha o eixo/orientação para posicionar o barco:\n")
        while eixo == -1:
            eixo = input("↔️ [HORIZONTAL] ou [X] | ↕️ [VERTICAL] ou [Y]: ").lower()
            print()
            eixo = converter_eixo(eixo)
    else:
        eixo = "x" # O eixo tem que ser alguma coisa para não ficar preso no loop de -1

    print_matriz_convertida(matrizBack, matrizFront, "posicionando", jogador) # Usa a matriz correta para exibir

    adicionar_barco_matriz(matrizBack, matrizFront, linha, coluna, tamanho, eixo, jogador)
    limpar_terminal()
    print_matriz_convertida(matrizBack, matrizFront, "posicionando", jogador)
    input("Pressione Enter para continuar...")
    limpar_terminal()


def posicionar_barco_computador(barco, matriz_computador_back):
    if barco == PORTA_AVIOES:
        tamanho = 5
    elif barco == NAVIO_TANQUE:
        tamanho = 4
    elif barco == CONTRATORPEDEIRO:
        tamanho = 3
    elif barco == SUBMARINO:
        tamanho = 2
    elif barco == DESTROIER:
        tamanho = 1
    else:
        print(f"ERRO! dev digitou barco inexistente! {barco}")
        return

    eixo = converter_eixo(random.randint(0,1))

    repetir = True
    id = tamanho

    while repetir:
        podePosicionar = True
        linha = random.randint(1,10)
        coluna = random.randint(1,10)

        if eixo == "x":
            for i in range(tamanho):
                if coluna > (12 - tamanho) or matriz_computador_back[linha][coluna+i] != 0:
                    podePosicionar = False
                    break # Sai do loop cedo se a posição for inválida
            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matriz_computador_back[linha][coluna+i] = id

        elif eixo == "y":
            for i in range(tamanho):
                if linha > (12 - tamanho) or matriz_computador_back[linha+i][coluna] != 0:
                    podePosicionar = False
                    break # Sai do loop cedo se a posição for inválida
            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matriz_computador_back[linha+i][coluna] = id


def input_jogador_atacar(atacante):
    linhaAtacar = -1
    colunaAtacar = -1

    print(f"🎯 Vez do {atacante} atacar!\n")
    time.sleep(.5)

    while linhaAtacar == -1:
        linhaAtacar = input("Digite a posição da LINHA (LETRA) para atacar!").lower()
        linhaAtacar = converter_caractere(linhaAtacar)

    while colunaAtacar == -1:
        colunaAtacar = input("Digite a posição da COLUNA (NUMERO) para atacar!").lower()
        colunaAtacar = converter_caractere(colunaAtacar)

    return linhaAtacar, colunaAtacar

def computador_atacar():
    print("💭 O computador está pensando!\n")
    time.sleep(.5)

    linhaAtacar = random.randint(1,10)
    colunaAtacar = random.randint(1,10)

    return linhaAtacar, colunaAtacar

def pre_jogo_humano(jogador_name, matriz_front, matriz_back):
    print(f"===== ⚠️  {jogador_name}, Lembre-se! ⚠️  =====\n")
    print("◽️ Ao escolher a orientação horizontal, sua embarcação será posicionada da esquerda para a direita.")
    print("◽️ Caso escolha a vertical, sua embarcação será posicionada de cima para baixo\n")
    input("Pressione Enter para começar a posicionar seus barcos...")
    limpar_terminal()

    # Pede para o humano posicionar os barcos
    posicionar_barco_jogador(PORTA_AVIOES, jogador_name, matriz_front, matriz_back) # tamanho 5
    posicionar_barco_jogador(NAVIO_TANQUE, jogador_name, matriz_front, matriz_back) # 4
    posicionar_barco_jogador(CONTRATORPEDEIRO, jogador_name, matriz_front, matriz_back) # 3
    posicionar_barco_jogador(SUBMARINO, jogador_name, matriz_front, matriz_back) # 2
    posicionar_barco_jogador(DESTROIER, jogador_name, matriz_front, matriz_back) # 1
    limpar_terminal()
    print(f"{jogador_name}, seus barcos foram posicionados com sucesso!")
    input("Pressione Enter para continuar...")
    limpar_terminal()

def print_tabuleiro_jogo(qtd_barcos_oponente, qtd_barcos_player, matriz_oponente_back, matriz_oponente_front, matriz_player_back, matriz_player_front, atacante, defensor):

    limpar_terminal()

    print_matriz_convertida(matriz_oponente_back, matriz_oponente_front, "jogando", defensor)
    print(f"{defensor} tem {qtd_barcos_oponente} barcos restantes\n")

    print("• = = = = = • = = = = = • = = = = = •\n")

    print_matriz_convertida(matriz_player_back, matriz_player_front, "jogando", atacante)
    print(f"{atacante} tem {qtd_barcos_player} barcos restantes\n")

    print("• = = = = = • = = = = = • = = = = = •\n")


def checar_fim(qtdBarcosJ1, qtdBarcosJ2):
    if qtdBarcosJ1 == 0:
        return COMPUTADOR # No single player, se o jogador 1 tem 0 barcos, a IA ganha
    elif qtdBarcosJ2 == 0:
        return HUMANO # No single player, se o jogador 2 (IA) tem 0 barcos, o jogador 1 ganha
    else:
        return "ninguem"

def checar_fim_pvp(qtdBarcosJ1, qtdBarcosJ2):
    if qtdBarcosJ1 == 0:
        return "Jogador 2" # Jogador 2 vence
    elif qtdBarcosJ2 == 0:
        return "Jogador 1" # Jogador 1 vence
    else:
        return "ninguem"

def inicio_jogo():
    # Matrizes globais para o jogo contra a IA
    global matrizJogadorFront, matrizJogadorBack, matrizComputadorFront, matrizComputadorBack

    matrizJogadorFront = criar_matriz_front()
    matrizJogadorBack = criar_matriz_back()
    matrizComputadorFront = criar_matriz_front()
    matrizComputadorBack = criar_matriz_back()

    pre_jogo_humano(HUMANO, matrizJogadorFront, matrizJogadorBack)

    print("🤖 Agora o computador vai posicionar os barcos! Aguarde...")
    time.sleep(1.5)
    posicionar_barco_computador(PORTA_AVIOES, matrizComputadorBack)
    posicionar_barco_computador(NAVIO_TANQUE, matrizComputadorBack)
    posicionar_barco_computador(CONTRATORPEDEIRO, matrizComputadorBack)
    posicionar_barco_computador(SUBMARINO, matrizComputadorBack)
    posicionar_barco_computador(DESTROIER, matrizComputadorBack)
    limpar_terminal()
    print("Computador posicionou os barcos!")
    input("Pressione Enter para começar o jogo...")
    limpar_terminal()


    qtdBarcosJ1 = 5 # Jogador 1 (Humano)
    qtdBarcosIa = 5 # Jogador 2 (IA)
    vidasBarcosJ1 = [5,4,3,2,1] # Vidas dos barcos do jogador humano
    vidasBarcosIa = [5,4,3,2,1] # Vidas dos barcos da IA
    vitoria = "ninguem"

    print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1, matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, HUMANO, COMPUTADOR)


    while vitoria == "ninguem":
        # JOGADA JOGADOR (HUMANO)
        jogada_valida_jogador = False
        while not jogada_valida_jogador:
            linhaAtacar, colunaAtacar = input_jogador_atacar(HUMANO)

            if matrizComputadorBack[linhaAtacar][colunaAtacar] == 6 or matrizComputadorBack[linhaAtacar][colunaAtacar] == 7:
                print("❌ Esta posição já foi atacada! Escolha uma posição válida!")
                continue
            else:
                jogada_valida_jogador = True

        barcoAtingido = verificar_acerto_tiro(matrizComputadorBack, matrizComputadorFront, linhaAtacar, colunaAtacar)

        if barcoAtingido is not None:
            acertou = True
            qtdBarcosIa, vidasBarcosIa, afundou = pegar_qtd_barcos(vidasBarcosIa, barcoAtingido)

            print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1, matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, HUMANO, COMPUTADOR)

            if afundou:
                print("☠️ Você afundou um navio inimigo! Você pode atacar novamente! 💥\n")
                vitoria = checar_fim(qtdBarcosJ1, qtdBarcosIa)
                if vitoria == HUMANO:
                    break # Jogador venceu, encerra o loop do jogo
                else:
                    # Jogador afundou um barco, então ele tem outro turno. Volta para o loop sem a vez da IA.
                    continue
            else:
                print(f"O(a) {HUMANO} ACERTOU o tiro! 💥 ")
        else:
            acertou = False
            print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1, matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, HUMANO, COMPUTADOR)
            print(f"O(a) {HUMANO} ERROU o tiro! 🌀 ")

        input("Pressione Enter para continuar...")

        vitoria = checar_fim(qtdBarcosJ1, qtdBarcosIa)
        if vitoria != "ninguem":
            break

        # JOGADA IA (COMPUTADOR)
        jogada_valida_ia = False
        while not jogada_valida_ia:
            linhaAtacar, colunaAtacar = computador_atacar()
            if matrizJogadorBack[linhaAtacar][colunaAtacar] == 6 or matrizJogadorBack[linhaAtacar][colunaAtacar] == 7:
                continue
            else:
                jogada_valida_ia = True

        barcoAtingido = verificar_acerto_tiro(matrizJogadorBack, matrizJogadorFront, linhaAtacar, colunaAtacar)

        if barcoAtingido is not None:
            acertou = True
            qtdBarcosJ1, vidasBarcosJ1, afundou = pegar_qtd_barcos(vidasBarcosJ1, barcoAtingido)

            print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1, matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, HUMANO, COMPUTADOR)

            if afundou:
                print(f"O {COMPUTADOR} AFUNDOU o navio e pode jogar novamente! 💥\n")
                vitoria = checar_fim(qtdBarcosJ1, qtdBarcosIa)
                if vitoria == COMPUTADOR:
                    break # IA venceu, encerra o loop do jogo
                else:
                    # IA afundou um barco, então ela tem outro turno. Volta para o loop da vez da IA.
                    continue
            else:
                print(f"\nO {COMPUTADOR} ACERTOU o tiro! 💥 \n")
        else:
            acertou = False
            print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1, matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, HUMANO, COMPUTADOR)
            print(f"\nO {COMPUTADOR} errou o tiro! 🌀 \n")

        input("Pressione Enter para continuar...")

        vitoria = checar_fim(qtdBarcosJ1, qtdBarcosIa)


    if vitoria == HUMANO:
        limpar_terminal()
        print("\n🥇 Parabéns!!! Você Ganhou!!!\n🙏 Muito obrigado por jogar!\n 🙅🙅🙅 Feito por Luis Quintliano, Davi cagnato, Larissa Adames ")
    elif vitoria == COMPUTADOR:
        limpar_terminal()
        print("😭 Não foi dessa vez amigo , você perdeu!\n🙏 Muito obrigado por jogar!\n🙅🙅🙅 Feito por Luis Quintliano, Davi cagnato, Larissa Adames")

def start_pvp_game():
    limpar_terminal()
    print("=============== MODO JOGADOR VS JOGADOR ===============\n")
    print("Preparando os tabuleiros para Jogador 1 e Jogador 2...\n")
    input("Pressione Enter para Jogador 1 posicionar seus barcos...")
    limpar_terminal()

    matrizJogador1Front = criar_matriz_front()
    matrizJogador1Back = criar_matriz_back()
    matrizJogador2Front = criar_matriz_front()
    matrizJogador2Back = criar_matriz_back()

    # Posicionamento do Jogador 1
    pre_jogo_humano("Jogador 1", matrizJogador1Front, matrizJogador1Back)

    # Posicionamento do Jogador 2
    print("Agora é a vez do Jogador 2 posicionar seus barcos.")
    input("Pressione Enter para Jogador 2 posicionar seus barcos...")
    limpar_terminal()
    pre_jogo_humano("Jogador 2", matrizJogador2Front, matrizJogador2Back)


    qtdBarcosJ1 = 5
    qtdBarcosJ2 = 5
    vidasBarcosJ1 = [5,4,3,2,1]
    vidasBarcosJ2 = [5,4,3,2,1]
    vitoria = "ninguem"

    while vitoria == "ninguem":
        # JOGADA JOGADOR 1
        jogada_valida_j1 = False
        while not jogada_valida_j1:
            limpar_terminal()
            print_matriz_convertida(matrizJogador2Back, matrizJogador2Front, "jogando", "Jogador 2 (Oponente)")
            print(f"Jogador 2 tem {qtdBarcosJ2} barcos restantes\n")
            print("• = = = = = • = = = = = • = = = = = •\n")
            print_matriz_convertida(matrizJogador1Back, matrizJogador1Front, "jogando", "Jogador 1 (Seu tabuleiro)")
            print(f"Jogador 1 tem {qtdBarcosJ1} barcos restantes\n")
            print("• = = = = = • = = = = = • = = = = = •\n")

            linhaAtacar, colunaAtacar = input_jogador_atacar("Jogador 1")

            if matrizJogador2Back[linhaAtacar][colunaAtacar] == 6 or matrizJogador2Back[linhaAtacar][colunaAtacar] == 7:
                print("❌ Esta posição já foi atacada! Escolha uma posição válida!")
                input("Pressione Enter para tentar novamente...")
                continue
            else:
                jogada_valida_j1 = True

        barcoAtingido = verificar_acerto_tiro(matrizJogador2Back, matrizJogador2Front, linhaAtacar, colunaAtacar)

        limpar_terminal()
        print_matriz_convertida(matrizJogador2Back, matrizJogador2Front, "jogando", "Jogador 2 (Oponente)")
        print(f"Jogador 2 tem {qtdBarcosJ2} barcos restantes\n")
        print("• = = = = = • = = = = = • = = = = = •\n")
        print_matriz_convertida(matrizJogador1Back, matrizJogador1Front, "jogando", "Jogador 1 (Seu tabuleiro)")
        print(f"Jogador 1 tem {qtdBarcosJ1} barcos restantes\n")
        print("• = = = = = • = = = = = • = = = = = •\n")

        if barcoAtingido is not None:
            acertou = True
            qtdBarcosJ2, vidasBarcosJ2, afundou = pegar_qtd_barcos(vidasBarcosJ2, barcoAtingido)

            if afundou:
                print("☠️ Jogador 1 afundou um navio do Jogador 2! Jogador 1 pode atacar novamente! 💥\n")
                vitoria = checar_fim_pvp(qtdBarcosJ1, qtdBarcosJ2)
                if vitoria != "ninguem":
                    break
                input("Pressione Enter para continuar...")
                continue # Jogador 1 ganha outro turno
            else:
                print(f"Jogador 1 ACERTOU o tiro! 💥 ")
        else:
            acertou = False
            print(f"Jogador 1 ERROU o tiro! 🌀 ")

        input("Pressione Enter para continuar...")

        vitoria = checar_fim_pvp(qtdBarcosJ1, qtdBarcosJ2)
        if vitoria != "ninguem":
            break

        # JOGADA JOGADOR 2
        jogada_valida_j2 = False
        while not jogada_valida_j2:
            limpar_terminal()
            print_matriz_convertida(matrizJogador1Back, matrizJogador1Front, "jogando", "Jogador 1 (Oponente)")
            print(f"Jogador 1 tem {qtdBarcosJ1} barcos restantes\n")
            print("• = = = = = • = = = = = • = = = = = •\n")
            print_matriz_convertida(matrizJogador2Back, matrizJogador2Front, "jogando", "Jogador 2 (Seu tabuleiro)")
            print(f"Jogador 2 tem {qtdBarcosJ2} barcos restantes\n")
            print("• = = = = = • = = = = = • = = = = = •\n")

            linhaAtacar, colunaAtacar = input_jogador_atacar("Jogador 2")

            if matrizJogador1Back[linhaAtacar][colunaAtacar] == 6 or matrizJogador1Back[linhaAtacar][colunaAtacar] == 7:
                print("❌ Esta posição já foi atacada! Escolha uma posição válida!")
                input("Pressione Enter para tentar novamente...")
                continue
            else:
                jogada_valida_j2 = True

        barcoAtingido = verificar_acerto_tiro(matrizJogador1Back, matrizJogador1Front, linhaAtacar, colunaAtacar)

        limpar_terminal()
        print_matriz_convertida(matrizJogador1Back, matrizJogador1Front, "jogando", "Jogador 1 (Oponente)")
        print(f"Jogador 1 tem {qtdBarcosJ1} barcos restantes\n")
        print("• = = = = = • = = = = = • = = = = = •\n")
        print_matriz_convertida(matrizJogador2Back, matrizJogador2Front, "jogando", "Jogador 2 (Seu tabuleiro)")
        print(f"Jogador 2 tem {qtdBarcosJ2} barcos restantes\n")
        print("• = = = = = • = = = = = • = = = = = •\n")

        if barcoAtingido is not None:
            acertou = True
            qtdBarcosJ1, vidasBarcosJ1, afundou = pegar_qtd_barcos(vidasBarcosJ1, barcoAtingido)

            if afundou:
                print("☠️ Jogador 2 afundou um navio do Jogador 1! Jogador 2 pode atacar novamente! 💥\n")
                vitoria = checar_fim_pvp(qtdBarcosJ1, qtdBarcosJ2)
                if vitoria != "ninguem":
                    break
                input("Pressione Enter para continuar...")
                continue # Jogador 2 ganha outro turno
            else:
                print(f"Jogador 2 ACERTOU o tiro! 💥 ")
        else:
            acertou = False
            print(f"Jogador 2 ERROU o tiro! 🌀 ")

        input("Pressione Enter para continuar...")

        vitoria = checar_fim_pvp(qtdBarcosJ1, qtdBarcosJ2)

    limpar_terminal()
    if vitoria == "Jogador 1":
        print("\n🥇 Parabéns Jogador 1!!! Você Ganhou!!!\n🙏 Muito obrigado por jogar!\n 🙅🙅🙅 Feito por Luis Quintliano, Davi cagnato, Larissa Adames ")
    elif vitoria == "Jogador 2":
        print("\n🥇 Parabéns Jogador 2!!! Você Ganhou!!!\n🙏 Muito obrigado por jogar!\n🙅🙅🙅 Feito por Luis Quintliano, Davi cagnato, Larissa Adames")


def menu():
    print("=============== Bem-vindo ao Batalha Naval! ===============\n")
    print("📑 Batalha naval é um jogo de tabuleiro de dois jogadores, no qual os jogadores têm de adivinhar em que quadrados estão os navios do oponente.\n")
    print("👉 Seu objetivo é derrubar os barcos do oponente adversário, ganha quem derrubar todos os navios adversários primeiro.")
    time.sleep(.5)
    print("\n=============== Escolha seu modo de jogo! ===============\n")

    while True:
        print("1. Jogar contra o Computador 🤖")
        print("2. Jogar contra outro Jogador (PvP) 🤝")
        print("3. Sair do Jogo 🚪")
        choice = input("Digite sua escolha (1, 2 ou 3): ").strip()

        if choice == '1':
            limpar_terminal()
            print("\n=============== Primeiro, você terá que posicionar os barcos no seu tabuleiro, siga as instruções: ===============\n")
            time.sleep(0.5)
            inicio_jogo()
            break
        elif choice == '2':
            start_pvp_game()
            break
        elif choice == '3':
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Escolha inválida. Por favor, digite 1, 2 ou 3.")
        time.sleep(1)
        limpar_terminal()


# Inicializando matrizes globais para o modo single player (movido para dentro de inicio_jogo)
matrizJogadorFront = []
matrizJogadorBack = []
matrizComputadorFront = []
matrizComputadorBack = []

menu()