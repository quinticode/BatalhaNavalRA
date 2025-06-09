# Batalha Naval - Código original com melhorias aplicadas de forma clara e compreensível
# Melhorias aplicadas:
# 1. Jogador ou computador ataca novamente se afundar navio
# 2. Evita ataques repetidos (verifica se célula já foi atingida)
# 3. Aleatoriza quem começa
# 4. Nome do barco atingido nas mensagens
# 5. Mostra tabuleiros finais e agradecimento completo

import random
import time

# Dicionário com os nomes dos barcos por tamanho
nomes_barcos = {
    5: "Porta-aviões",
    4: "Navio-tanque",
    3: "Contratorpedeiro",
    2: "Submarino",
    1: "Destroier"
}

letras = {chr(97 + i): i + 1 for i in range(10)}
def converter_caractere(caractere):
    caractere = caractere.lower()
    if caractere in letras:
        return letras[caractere]
    elif caractere.isdigit() and 1 <= int(caractere) <= 10:
        return int(caractere)
    else:
        print("Digite uma posição válida!")
        return -1

def verificar_numero(numero):
    if 1 <= numero <= 10:
        return numero
    else:
        return -1

def converter_eixo(eixo):
    if eixo in ["horizontal", "x", "h", 0]:
        return "x"
    elif eixo in ["vertical", "y", "v", 1]:
        return "y"
    else:
        print("\nDigite um valor válido!\n")
        return -1

def criar_11x11_front():
    return [["-" if i == 0 and j == 0 else chr(64+i) if j == 0 else str(j) if i == 0 else "🌊" for j in range(11)] for i in range(11)]

def criar_matriz_back():
    return [[-1 if i == 0 or j == 0 or i == 11 or j == 11 else 0 for j in range(12)] for i in range(12)]

def criar_vidas_barcos():
    return [1, 2, 3, 4, 5]

def pegar_qtd_barcos(vidaBarcos, barcoAtingido):
    afundouBarco = False
    qtdBarcos = 0
    for i in range(len(vidaBarcos)):
        if (i + 1) == barcoAtingido:
            vidaBarcos[i] -= 1
            if vidaBarcos[i] == 0:
                afundouBarco = True
        if vidaBarcos[i] > 0:
            qtdBarcos += 1
    return qtdBarcos, vidaBarcos, afundouBarco

def input_coord():
    linha = -1
    coluna = -1
    while linha == -1:
        linha = input("Digite a LINHA (LETRA): ").strip().lower()
        linha = converter_caractere(linha)
    while coluna == -1:
        coluna = input("Digite a COLUNA (NUMERO): ").strip().lower()
        coluna = converter_caractere(coluna)
        coluna = verificar_numero(coluna)
    return linha, coluna

def verificar_acerto_tiro(matrizBack, matrizFront, linha, coluna):
    if matrizBack[linha][coluna] in [6, 7]:
        return "repetido", None
    elif matrizBack[linha][coluna] > 0:
        barcoAtingido = matrizBack[linha][coluna]
        matrizBack[linha][coluna] = 6
        matrizFront[linha][coluna] = '💥'
        return "acerto", barcoAtingido
    else:
        matrizBack[linha][coluna] = 7
        matrizFront[linha][coluna] = '🌀'
        return "erro", None

def print_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(c) for c in linha))

def print_tabuleiro_jogo(matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, qtdBarcosIa, qtdBarcosJ1):
    print("\n--- TABULEIROS ATUAIS ---")
    print("\nComputador:")
    print_matriz(matrizComputadorFront)
    print(f"Barcos restantes: {qtdBarcosIa}\n")
    print("Jogador:")
    print_matriz(matrizJogadorFront)
    print(f"Barcos restantes: {qtdBarcosJ1}")

def checar_fim(qtdBarcosIa, qtdBarcosJ1):
    if qtdBarcosIa == 0:
        return "Jogador"
    elif qtdBarcosJ1 == 0:
        return "Computador"
    else:
        return "nao"

def inicio_jogo():
    matrizJogadorFront = criar_11x11_front()
    matrizJogadorBack = criar_matriz_back()
    matrizComputadorFront = criar_11x11_front()
    matrizComputadorBack = criar_matriz_back()

    vidaJogador = criar_vidas_barcos()
    vidaComputador = criar_vidas_barcos()
    qtdBarcosJogador = 5
    qtdBarcosComputador = 5

    print("Posicione seus navios:")
    for tamanho in [5, 4, 3, 2, 1]:
        print(f"\nPosicione o {nomes_barcos[tamanho]} (tamanho {tamanho})")
        eixo = -1
        while eixo == -1:
            eixo_input = input("Eixo (horizontal/vertical): ")
            eixo = converter_eixo(eixo_input)
        adicionar_barco(matrizJogadorBack, tamanho, eixo, rand=False)

    print("\nComputador posicionando...")
    for tamanho in [5, 4, 3, 2, 1]:
        eixo = converter_eixo(random.choice(["x", "y"]))
        adicionar_barco(matrizComputadorBack, tamanho, eixo, rand=True)

    turno = random.choice(["Jogador", "Computador"])
    print(f"\n{turno} começa o jogo!")

    vencedor = "nao"
    while vencedor == "nao":
        if turno == "Jogador":
            print("\nSua vez de atacar:")
            jogando = True
            while jogando:
                linha, coluna = input_coord()
                status, tipo = verificar_acerto_tiro(matrizComputadorBack, matrizComputadorFront, linha, coluna)
                if status == "repetido":
                    print("Você já atacou essa posição. Tente outra.")
                    continue
                elif status == "acerto":
                    print(f"💥 Você acertou um {nomes_barcos[tipo]}!")
                    qtdBarcosComputador, vidaComputador, afundou = pegar_qtd_barcos(vidaComputador, tipo)
                    if afundou:
                        print("🚢 Você afundou um navio inimigo! Pode jogar novamente.")
                        print_tabuleiro_jogo(matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, qtdBarcosComputador, qtdBarcosJogador)
                        if checar_fim(qtdBarcosComputador, qtdBarcosJogador) != "nao":
                            vencedor = "Jogador"
                            break
                        continue
                else:
                    print("🌀 Você errou o ataque.")
                jogando = False
                turno = "Computador"
        else:
            print("\nVez do Computador:")
            jogando = True
            while jogando:
                linha = random.randint(1,10)
                coluna = random.randint(1,10)
                status, tipo = verificar_acerto_tiro(matrizJogadorBack, matrizJogadorFront, linha, coluna)
                if status == "repetido":
                    continue
                elif status == "acerto":
                    print(f"💥 O Computador acertou seu {nomes_barcos[tipo]}!")
                    qtdBarcosJogador, vidaJogador, afundou = pegar_qtd_barcos(vidaJogador, tipo)
                    if afundou:
                        print("🚢 O Computador afundou um navio seu e jogará novamente!")
                        print_tabuleiro_jogo(matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, qtdBarcosComputador, qtdBarcosJogador)
                        if checar_fim(qtdBarcosComputador, qtdBarcosJogador) != "nao":
                            vencedor = "Computador"
                            break
                        continue
                else:
                    print("🌀 O Computador errou.")
                jogando = False
                turno = "Jogador"

        print_tabuleiro_jogo(matrizComputadorBack, matrizComputadorFront, matrizJogadorBack, matrizJogadorFront, qtdBarcosComputador, qtdBarcosJogador)
        vencedor = checar_fim(qtdBarcosComputador, qtdBarcosJogador)

    print(f"\n🏆 {vencedor.upper()} venceu o jogo! Parabéns!")
    print("Créditos: Luis Felipe Quintiliano, Davi Cagnato, Larissa Adames")

# Função auxiliar para posicionar embarcações

def adicionar_barco(matriz, tamanho, direcao, rand=False):
    while True:
        if rand:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 10)
        else:
            linha, coluna = input_coord()

        pode_posicionar = True
        if direcao == "x" and coluna + tamanho - 1 <= 10:
            for i in range(tamanho):
                if matriz[linha][coluna + i] != 0:
                    pode_posicionar = False
            if pode_posicionar:
                for i in range(tamanho):
                    matriz[linha][coluna + i] = tamanho
                break
        elif direcao == "y" and linha + tamanho - 1 <= 10:
            for i in range(tamanho):
                if matriz[linha + i][coluna] != 0:
                    pode_posicionar = False
            if pode_posicionar:
                for i in range(tamanho):
                    matriz[linha + i][coluna] = tamanho
                break
        if not rand:
            print("Posição inválida ou já ocupada. Tente novamente.")

inicio_jogo()
