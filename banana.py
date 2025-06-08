# Batalha Naval com otimizações mínimas e cores por embarcação
import random
import time

# Conversão de letra ou número textual para coordenada numérica
letras = {chr(97 + i): i + 1 for i in range(10)}  # 'a' até 'j' => 1 a 10
numeros = {str(i): i for i in range(1, 11)}
def converter_caractere(c):
    c = c.lower()
    return letras.get(c, numeros.get(c, -1))

def verificar_numero(n):
    return n if 0 < n <= 10 else -1

def converter_eixo(eixo):
    eixo = str(eixo).lower()
    if eixo in ["horizontal", "x", "h", "0"]:
        return "x"
    elif eixo in ["vertical", "y", "v", "1"]:
        return "y"
    return -1

def criar_11x11_front():
    return [["-" if i == 0 and j == 0 else chr(64+i) if j == 0 else f"{j:2}" if i == 0 else "🌊" for j in range(11)] for i in range(11)]

def criar_matriz_back():
    return [[-1 if i == 0 or j == 0 or i == 11 or j == 11 else 0 for j in range(12)] for i in range(12)]

def criar_vidas_barcos():
    return [1,2,3,4,5]  # Destroier até Porta-aviões

cores_barcos = {
    1: "🟧",  # Destroier
    2: "🟨",  # Submarino
    3: "🟩",  # Contratorpedeiro
    4: "🟥",  # Navio-tanque
    5: "⬜️",  # Porta-aviões
}

matrizJogadorFront = criar_11x11_front()
matrizJogadorBack = criar_matriz_back()
matrizComputadorFront = criar_11x11_front()
matrizComputadorBack = criar_matriz_back()

def pegar_qtd_barcos(vidaBarcos,barcoAtingido):
    qtdBarcos = 0
    afundouBarco = False
    for i, vida in enumerate(vidaBarcos):
        if i + 1 == barcoAtingido:
            vidaBarcos[i] -= 1
            if vidaBarcos[i] == 0:
                afundouBarco = True
        if vidaBarcos[i] > 0:
            qtdBarcos += 1
    return qtdBarcos, vidaBarcos, afundouBarco

def print_matriz(matriz):
    print("\n" + "\n".join(" ".join(str(c) for c in linha) for linha in matriz) + "\n")

def input_coord():
    while True:
        linha = converter_caractere(input("Linha (letra): "))
        if linha != -1:
            break
    while True:
        coluna = verificar_numero(converter_caractere(input("Coluna (número): ")))
        if coluna != -1:
            break
    return linha, coluna

def verificar_acerto_tiro(matrizBack, matrizFront, linha, coluna):
    if matrizBack[linha][coluna] not in [0, -1, 6, 7]:
        barco = matrizBack[linha][coluna]
        matrizBack[linha][coluna] = 6
        matrizFront[linha][coluna] = '💥'
        return barco
    elif matrizBack[linha][coluna] == 0:
        matrizBack[linha][coluna] = 7
        matrizFront[linha][coluna] = '🌀'

def adicionar_barco_matriz(matriz, tamanho, direcao, input_func=input_coord):
    while True:
        linha, coluna = input_func()
        if direcao == "x" and coluna + tamanho - 1 <= 10:
            if all(matriz[linha][coluna + i] == 0 for i in range(tamanho)):
                for i in range(tamanho):
                    matriz[linha][coluna + i] = tamanho
                break
        elif direcao == "y" and linha + tamanho - 1 <= 10:
            if all(matriz[linha + i][coluna] == 0 for i in range(tamanho)):
                for i in range(tamanho):
                    matriz[linha + i][coluna] = tamanho
                break
        print("Posição inválida ou ocupada. Tente novamente.")

def print_matriz_convertida(matrizIn, matrizOut, situacao, jogador):
    for i in range(1,11):
        for j in range(1,11):
            if situacao == "posicionando" and matrizIn[i][j] in cores_barcos:
                matrizOut[i][j] = cores_barcos[matrizIn[i][j]]
            elif situacao == "jogando" and matrizOut[i][j] not in ["💥", "🌀"]:
                matrizOut[i][j] = "🌊"
    print(f"\nTabuleiro do {jogador}:")
    print_matriz(matrizOut)

def posicionar_barco_jogador(nome, tamanho):
    print(f"\nPosicione o {nome} (Tamanho: {tamanho})")
    while True:
        eixo = converter_eixo(input("Eixo (x/y): "))
        if eixo != -1:
            break
    print_matriz(matrizJogadorFront)
    adicionar_barco_matriz(matrizJogadorBack, tamanho, eixo)
    print_matriz_convertida(matrizJogadorBack, matrizJogadorFront, "posicionando", "Jogador")

def posicionar_barco_computador(tamanho):
    eixo = converter_eixo(random.choice(["x", "y"]))
    def rand_coord(): return random.randint(1,10), random.randint(1,10)
    adicionar_barco_matriz(matrizComputadorBack, tamanho, eixo, rand_coord)

def print_tabuleiro_jogo(qtdCpu, qtdJog):
    print_matriz_convertida(matrizComputadorBack, matrizComputadorFront, "jogando", "Computador")
    print(f"Computador tem {qtdCpu} barcos restantes\n")
    print_matriz_convertida(matrizJogadorBack, matrizJogadorFront, "jogando", "Jogador")
    print(f"Jogador tem {qtdJog} barcos restantes\n")

def checar_fim(qtdCpu,qtdJog):
    return "Jogador" if qtdCpu == 0 else "Computador" if qtdJog == 0 else "nao"

def pre_jogo():
    for nome, tam in zip(["PORTA-AVIÕES","NAVIO-TANQUE","CONTRATORPEDEIRO","SUBMARINO","DESTROIER"],[5,4,3,2,1]):
        posicionar_barco_jogador(nome, tam)
    print("\nComputador posicionando embarcações...")
    time.sleep(1)
    for tam in [5,4,3,2,1]:
        posicionar_barco_computador(tam)

def inicio_jogo():
    pre_jogo()
    qtdJog = qtdCpu = 5
    vidaJog = criar_vidas_barcos()
    vidaCpu = criar_vidas_barcos()
    vitoria = "nao"

    while vitoria == "nao":
        while True:
            l,c = input_coord()
            if matrizComputadorBack[l][c] in [6,7]:
                print("Já atacado. Escolha outro.")
                continue
            barco = verificar_acerto_tiro(matrizComputadorBack, matrizComputadorFront, l, c)
            if barco:
                print("💥 Acertou!")
                qtdCpu, vidaCpu, afundou = pegar_qtd_barcos(vidaCpu, barco)
                if afundou:
                    print("🚢 Afundou! Ataca novamente.")
                    print_tabuleiro_jogo(qtdCpu, qtdJog)
                    if checar_fim(qtdCpu,qtdJog)!="nao":
                        break
                    continue
            else:
                print("🌀 Errou!")
            break
        print_tabuleiro_jogo(qtdCpu, qtdJog)
        vitoria = checar_fim(qtdCpu,qtdJog)
        if vitoria != "nao": break
        input("Enter para continuar")
        while True:
            l,c = random.randint(1,10), random.randint(1,10)
            if matrizJogadorBack[l][c] in [6,7]: continue
            barco = verificar_acerto_tiro(matrizJogadorBack, matrizJogadorFront, l, c)
            if barco:
                print("💥 Computador acertou!")
                qtdJog, vidaJog, afundou = pegar_qtd_barcos(vidaJog, barco)
                if afundou:
                    print("🚢 Computador afundou um navio. Atacará de novo!")
                    print_tabuleiro_jogo(qtdCpu, qtdJog)
                    if checar_fim(qtdCpu,qtdJog)!="nao":
                        break
                    continue
            else:
                print("🌀 Computador errou.")
            break
        print_tabuleiro_jogo(qtdCpu, qtdJog)
        vitoria = checar_fim(qtdCpu,qtdJog)

    print(f"\n🎉 {vitoria.upper()} venceu! Parabéns!\nCréditos: Luis Felipe, Davi Cagnato, Larissa Adames")

inicio_jogo()
