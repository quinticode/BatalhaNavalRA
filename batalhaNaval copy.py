# humano x compuador
# Cada jogador deve ter um tabuleiro (matriz) de tamanho 5x10 ou 10x10 que irá conter as informações
# das coordenadas de cada embarcação, também deverá ter outro tabuleiro (matriz vazia) de tamanho
# 5x10 ou 10x10 (um para o computador e outro para o jogador) que será exibido como feedback
# (impresso no console), esse segundo tabuleiro não deve possuir as informações de coordenadas
# (preencha a matriz com zeros ou qualquer outro caractere que achar adequado). As embarcações devem
# ocupar um único espaço da matriz. No mínimo 5 embarcações devem ser posicionadas.
#
# Ao iniciar o jogo, o programa deve solicitar ao jogador todas as coordenadas (linha e coluna) em que serão
# posicionadas as suas embarcações. As coordenadas das embarcações do computador devem ser definidas
# de forma aleatória (random). Essas coordenadas deverão ser armazenadas nos tabuleiros que não serão
# exibidos ao jogador. Depois de definir as posições, o programa deve exibir os dois tabuleiros sem
# informação das coordenadas de embarcação e a quantidade de embarcações em cada um dos tabuleiros,
# especificando qual tabuleiro pertence ao computador e qual pertence ao jogador. Em seguida um dos
# jogadores (humano ou computador) deve realizar seu ataque informando qual coordenada do tabuleiro do
# adversário deseja atacar. Após o ataque, o tabuleiro adversário que está sendo exibido deve ser atualizado
# no console, indicando que determinada posição já foi atacada. Caso o ataque tenha atingido uma
# embarcação inimiga, atualize o caractere na coordenada do tabuleiro exibido para X (sugestão) e escreva
# uma mensagem ao usuário indicando que houve um acerto de embarcação e quantas embarcações ainda
# restam. Não esqueça de atualizar também a quantidade de embarcações restantes no tabuleiro atingido.
# Caso o ataque não tenha atingido uma embarcação inimiga, atualize o caractere na coordenada do
# tabuleiro exibido para O (sugestão) e escreva uma mensagem ao usuário que não houve acerto em
# nenhuma embarcação inimiga.
# Quando um dos jogadores conseguir afundar toda a frota inimiga, o programa informa a vitória do jogador
# vencedor, exibe agradecimentos ao jogador humano e o nome dos integrantes da equipe e encerra o
# programa.
#
# Desafio (nota extra): Implementar o jogo batalha naval original, de forma que possua todas as
# embarcações, sendo elas: Porta-aviões (ocupando 5 posições), Navio-tanque (ocupando 4
# posições), Contratorpedeiro (ocupando 3 posições), Submarino (ocupando duas posições) e
# Destroier (ocupando 1 posição). Neste modo a embarcação só afunda quando todas as posições
# dela tiverem sido atingidas. Quando uma embarcação tiver todas as suas partes atingidas, a
# embarcação é então afundada e o jogador pode atacar novamente.

import random
import time

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
        print("Digite uma posição válida!")
        return -1
    
def verificar_numero(numero): # para a pessoa nao digitar "A" e sair como "1" na coluna, por exemplo

    if numero >= 0 and numero <= 10:
        return numero
    else:
        return -1

def converter_eixo(eixo):
    if eixo == "horizontal" or eixo == "x" or eixo == "h" or eixo == 0:
        return "x"
    elif eixo == "vertical" or eixo == "y" or eixo == "v" or eixo == 1:
        return "y"
    else:
        print("\nDigite um valor válido!\n")
        return -1

def criar_11x11_front():

    # return [
    # ['-','1','2','3','4','5','6','7','8','9','10'],
    # ['A','0','0','0','0','0','0','0','0','0','0'],
    # ['B','0','0','0','0','0','0','0','0','0','0'],
    # ['C','0','0','0','0','0','0','0','0','0','0'],
    # ['D','0','0','0','0','0','0','0','0','0','0'],
    # ['E','0','0','0','0','0','0','0','0','0','0'],
    # ['F','0','0','0','0','0','0','0','0','0','0'],
    # ['G','0','0','0','0','0','0','0','0','0','0'],
    # ['H','0','0','0','0','0','0','0','0','0','0'],
    # ['I','0','0','0','0','0','0','0','0','0','0'],
    # ['J','0','0','0','0','0','0','0','0','0','0'],
    # ]

    return [
    ['-',' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10'],
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
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #1
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1], #2
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

def criar_vidas_barcos():
    return [1,2,3,4,5]

def pegar_qtd_barcos(vidaBarcos,barcoAtingido): #

    qtdBarcos = 0

    for i in range(len(vidaBarcos)): # percorre as listas de vidas de barcos
        listaBarcos = [1,2,3,4,5]
        afundouBarco = False
        # vidas dos barcos: [1,2,3,4,5]

        if listaBarcos[i] == barcoAtingido: # se a posicao da lista for igual ao id do barcoAtingido, 
            vidaBarcos[i] -= 1 # entao ele subtrai um ponto de vida daquele tipo do barco
            if vidaBarcos[i] == 0:
                afundouBarco = True

        if vidaBarcos[i] != 0: # se a vida do barco nao for 0, ele ainda está vivo, entao aumenta a qtdBarcos
            qtdBarcos += 1
    
    return qtdBarcos, vidaBarcos, afundouBarco

def print_matriz(matriz):

    print()
    for i in range(len(matriz)):
        print(matriz[i])
    print()

def input_coord():

    linha = -1
    coluna = -1
        
    while linha == -1:
        linha = input("Digite a LINHA (LETRA) da posição aqui: ").strip().lower()
        linha = converter_caractere(linha)

    while coluna == -1:
        coluna = input("Digite a COLUNA (NUMERO) da posição aqui: ").strip().lower()
        coluna = converter_caractere(coluna)
        coluna = verificar_numero(coluna)
    
    return linha, coluna

matrizJogadorFront = criar_11x11_front() 
matrizJogadorBack = criar_matriz_back()
matrizComputadorFront = criar_11x11_front()
matrizComputadorBack = criar_matriz_back()

def verificar_acerto_tiro(matrizBack, matrizFront, linha, coluna):

    if matrizBack[linha][coluna] != 0 and matrizBack[linha][coluna] != -1 and matrizBack[linha][coluna] != 7 and matrizBack[linha][coluna] != 6: # <- ISSO SIGNIFICA QUE ACERTOU EM UM BARCO
        barcoAtingido = matrizBack[linha][coluna] # <- pega o tipo do barco que foi atingido e salva na variável barcoAtingido
        matrizBack[linha][coluna] = 6 # <- poe 6 na matriz back do que foi atingido
        matrizFront[linha][coluna] = '💥' 
        return barcoAtingido

    elif matrizBack[linha][coluna] == 0:
        matrizBack[linha][coluna] = 7
        matrizFront[linha][coluna] = '🌀'
                
def verificar_posicao(matriz, linha, coluna):
    if matriz[linha][coluna] != 0:
        print("Local já ocupado!")

def adicionar_barco_matriz(matriz,linha,coluna,tamanho,direcao):
        
        repetir = True # o jeito menos pior que consegui fazer pra repetir

        id = tamanho # só pra ficar mais claro. o número que aparece na matriz é o id do barco. por convenção decidi deixar como o tamanho dele.
            
        while repetir:

            podePosicionar = True # isso verifica se o barco pode ser posicionado. se nao puder, ele vira falso

            linha, coluna = input_coord() # pega o input da linha e da coluna

            if direcao == "x": # eixo horizontal

                for i in range(tamanho):
                    if coluna > (12 - tamanho) or matriz[linha][coluna+i] != 0: # se ele sair do tabuleiro, ou bater num barco, ele seta podePosicionar como falso
                        podePosicionar = False
                        
                if podePosicionar: # verifica se passou no teste ali atras
                    repetir = False
                    for i in range(tamanho): # poe o barco na horizontal, com o id dele na matriz
                        matriz[linha][coluna+i] = id

                else:
                    print("O seu barco está saindo do tabuleiro ou colidindo com outro barco! Escolha uma posição válida!")

            elif direcao == "y":
                for i in range(tamanho):
                    if linha > (12 - tamanho) or matriz[linha+i][coluna] != 0: # se ele sair do tabuleiro, ou bater num barco, ele seta podePosicionar como falso
                        podePosicionar = False

                if podePosicionar: # verifica se passou no teste ali atras
                    repetir = False
                    for i in range(tamanho): # poe o barco na vertical, com o id dele na matriz
                        matriz[linha+i][coluna] = id

                else:
                    print("O seu barco está saindo do tabuleiro ou colidindo com outro barco! Escolha uma posição válida!")

def print_matriz_convertida(matrizIn, matrizOut, situacao, jogador): # nao gosto dessa soluçao, percorre toda a matriz(sem contar a legenda) e vai convertendo os simbolos

    print(f"Tabuleiro do {jogador}")
    if situacao == "posicionando":
        for linha in range(1,11):
            for coluna in range(1,11):
                if matrizIn[linha][coluna] == 5:
                    matrizOut[linha][coluna] = "⬜️"
                elif matrizIn[linha][coluna] == 4:
                    matrizOut[linha][coluna] = "🟥"
                elif matrizIn[linha][coluna] == 3:
                    matrizOut[linha][coluna] = "🟩"
                elif matrizIn[linha][coluna] == 2:
                    matrizOut[linha][coluna] = "🟨"
                elif matrizIn[linha][coluna] == 1:
                    matrizOut[linha][coluna] = "🟧"
    
    elif situacao == "jogando": 
        
        for linha in range(1,11): 
            for coluna in range(1,11):
                if matrizOut[linha][coluna] == "⬜️" or matrizOut[linha][coluna] == "🟥" or matrizOut[linha][coluna] == "🟩" or matrizOut[linha][coluna] == "🟨" or matrizOut[linha][coluna] == "🟧": # aiai
                    matrizOut[linha][coluna] = "🌊"

        #         if matrizIn[linha][coluna] == 6:
        #             matrizOut[linha][coluna] = '💥'
        #         elif matrizIn[linha][coluna] == 7:
        #             matrizOut[linha][coluna] = '🌀'
        #         else:
        #             matrizOut[linha][coluna] = '🌊'

    return print_matriz(matrizOut)


def posicionar_barco_jogador(barco,jogador):

    if barco == "PORTA-AVIÕES":
        tamanho = 5
    elif barco == "NAVIO-TANQUE":
        tamanho = 4
    elif barco == "CONTRATORPEDEIRO":
        tamanho = 3
    elif barco == "SUBMARINO":
        tamanho = 2
    elif barco == "DESTROIER":
        tamanho = 1
    else:
        print(f"ERRO! dev digitou barco inexistente! {barco}")

    if jogador == "humano1":
        matrizFront = matrizJogadorFront
        matrizBack = matrizJogadorBack

    eixo = -1 # isso aqui é pra fazer loop caso o usuário digite um valor inadequado, adicionei funcoes que retornam -1 nesses casos.
    linha = -1
    coluna = -1

    print(f"Você está posicionando o {barco}, ele possui TAMANHO {tamanho}")

    print("Escolha o eixo para posicionar o barco: ")
    print("[HORIZONTAL] ou [x] | [VERTICAL] ou [y]\n")

    while eixo == -1:
        eixo = input("Escolha o eixo: ").lower()
        eixo = converter_eixo(eixo)

    print_matriz(matrizFront)

    adicionar_barco_matriz(matrizBack,linha,coluna,tamanho,eixo) # <- input_coord() ta aqui dentro
    print_matriz_convertida(matrizBack,matrizFront,"posicionando","Jogador")

def posicionar_barco_computador(barco):

    if barco == "PORTA-AVIÕES":
        tamanho = 5
    elif barco == "NAVIO-TANQUE":
        tamanho = 4
    elif barco == "CONTRATORPEDEIRO":
        tamanho = 3
    elif barco == "SUBMARINO":
        tamanho = 2
    elif barco == "DESTROIER":
        tamanho = 1
    else:
        print(f"ERRO! dev digitou barco inexistente! {barco}")

    eixo = converter_eixo(random.randint(0,1))
    
    repetir = True

    id = tamanho

    while repetir:

        podePosicionar = True

        linha = random.randint(1,10)
        coluna = random.randint(1,10)

        if eixo == "x":
            for i in range(tamanho):
                if coluna > (12 - tamanho) or matrizComputadorBack[linha][coluna+i] != 0:
                    podePosicionar = False

            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matrizComputadorBack[linha][coluna+i] = id
        
        elif eixo == "y":
            for i in range(tamanho):
                if linha > (12 - tamanho) or matrizComputadorBack[linha+i][coluna] != 0:
                    podePosicionar = False

            if podePosicionar:
                repetir = False
                for i in range(tamanho):
                    matrizComputadorBack[linha+i][coluna] = id
        
def input_jogador_atacar(jogador):

    linhaAtacar = -1
    colunaAtacar = -1

    while linhaAtacar == -1:
        linhaAtacar = input("Digite a posição da LINHA (LETRA) para atacar!")
        linhaAtacar = converter_caractere(linhaAtacar)

    while colunaAtacar == -1:
        colunaAtacar = input("Digite a posição da COLUNA (NUMERO) para atacar!")
        colunaAtacar = converter_caractere(colunaAtacar)

    return linhaAtacar, colunaAtacar

def input_computador_atacar():

    linhaAtacar = random.randint(1,10)
    colunaAtacar = random.randint(1,10)

    return linhaAtacar, colunaAtacar

def pre_jogo():

    # Pede para o humano posicionar os barcos
    posicionar_barco_jogador("PORTA-AVIÕES","humano1") # tamanho 5
    posicionar_barco_jogador("NAVIO-TANQUE","humano1") # 4
    posicionar_barco_jogador("CONTRATORPEDEIRO","humano1") # 3
    posicionar_barco_jogador("SUBMARINO","humano1") # 2
    posicionar_barco_jogador("DESTROIER","humano1") # 1

    print("Agora o computador vai posicionar os barcos! Aguarde...")
    time.sleep(.5)
    # Faz o computador posicionar os barcos
    posicionar_barco_computador("PORTA-AVIÕES")
    posicionar_barco_computador("NAVIO-TANQUE")
    posicionar_barco_computador("CONTRATORPEDEIRO")
    posicionar_barco_computador("SUBMARINO")
    posicionar_barco_computador("DESTROIER")

def print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1):
        
        print_matriz_convertida(matrizComputadorBack,matrizComputadorFront,"jogando", "computador")

        print(f"Computador tem {qtdBarcosIa} barcos restantes")

        print("=============================")

        print_matriz_convertida(matrizJogadorBack,matrizJogadorFront,"jogando", "jogador")

        print(f"Jogador tem {qtdBarcosJ1} barcos restantes")
        
        print("=============================")

def checar_fim(qtdBarcosIa,qtdBarcosJ1):

    if qtdBarcosIa == 0:
        return "Jogador" # jogador ganhou
    elif qtdBarcosJ1 == 0:
        return "Computador" # computador ganhou
    
    return "nao" # ninguem ganhou

def inicio_jogo():

    pre_jogo() # posicionamento dos barcos

    qtdBarcosJ1 = 5
    qtdBarcosIa = 5
    vidaBarcosJ1 = criar_vidas_barcos()
    vidaBarcosIa = criar_vidas_barcos()
    vitoria = "nao"

    # DIZ QUEM JOGOU, E SE ACERTOU
    # PRINTA MATRIZ COMPUTADOR
    # DIZ QUANTOS BARCOS COMPUTADOR
    # PRINTA MATRIZ HUMANO
    # DIZ QUANTOS BARCOS HUMANO


    print_matriz_convertida(matrizComputadorBack,matrizComputadorFront,"jogando", "computador")
    print_matriz(matrizComputadorBack) # se quiser testar tira o comentario
    print_matriz_convertida(matrizJogadorBack,matrizJogadorFront,"jogando", "jogador")
    print_matriz(matrizJogadorBack)

    while vitoria == "nao":

        # VEZ DO JOGADOR
        jogando = True
        while jogando:
            linhaAtacar, colunaAtacar = input_jogador_atacar("jogador1")
            if matrizComputadorBack[linhaAtacar][colunaAtacar] in [6, 7]:
                print("Você já atacou essa posição. Tente outra.")
                continue

            barcoAtingido = verificar_acerto_tiro(matrizComputadorBack, matrizComputadorFront, linhaAtacar, colunaAtacar)
            if barcoAtingido is not None:
                qtdBarcosIa, vidaBarcosIa, afundou = pegar_qtd_barcos(vidaBarcosIa, barcoAtingido)
                print("💥 Acertou!")
                if afundou:
                    print("🚢 Você afundou um navio! Jogue novamente.")
                    print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1)
                    vitoria = checar_fim(qtdBarcosIa, qtdBarcosJ1)
                    if vitoria != "nao":
                        break
                    continue
            else:
                print("🌀 Errou.")

            jogando = False

        if vitoria != "nao":
            break

        input("Enter para continuar")

        # VEZ DO COMPUTADOR
        jogando = True
        while jogando:
            linhaAtacar, colunaAtacar = input_computador_atacar()
            if matrizJogadorBack[linhaAtacar][colunaAtacar] in [6, 7]:
                continue  # tenta outro

            barcoAtingido = verificar_acerto_tiro(matrizJogadorBack, matrizJogadorFront, linhaAtacar, colunaAtacar)
            if barcoAtingido is not None:
                qtdBarcosJ1, vidaBarcosJ1, afundou = pegar_qtd_barcos(vidaBarcosJ1, barcoAtingido)
                print("💥 Computador acertou!")
                if afundou:
                    print("🚢 O computador afundou um navio e vai atacar novamente!")
                    print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1)
                    vitoria = checar_fim(qtdBarcosIa, qtdBarcosJ1)
                    if vitoria != "nao":
                        break
                    continue
            else:
                print("🌀 Computador errou.")

            jogando = False

        print_tabuleiro_jogo(qtdBarcosIa, qtdBarcosJ1)
        vitoria = checar_fim(qtdBarcosIa, qtdBarcosJ1)

    if vitoria == "Jogador":
        print("Parabéns!!! vc ganhou feito por luis felipe quintliano, davi cagnato, larissa adames")
    elif vitoria == "Computador":
        print("Não foi dessa vez amigo! feito por luis felipe quintliano, davi cagnato, larissa adames")

inicio_jogo()