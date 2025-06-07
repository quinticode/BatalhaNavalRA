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
import tkinter as tk

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
    if eixo == "horizontal" or eixo == "x" or eixo == "h":
        return "x"
    elif eixo == "vertical" or eixo == "y" or eixo == "v":
        return "y"
    else:
        print("\nDigite um valor válido!\n")
        return -1

def criar_11x11_front(): # <-- isso aqui é gambiarra pra fazer o 10x10 com feedback pro usuario

    return [
    ['-','1','2','3','4','5','6','7','8','9','10'],
    ['A','0','0','0','0','0','0','0','0','0','0'],
    ['B','0','0','0','0','0','0','0','0','0','0'],
    ['C','0','0','0','0','0','0','0','0','0','0'],
    ['D','0','0','0','0','0','0','0','0','0','0'],
    ['E','0','0','0','0','0','0','0','0','0','0'],
    ['F','0','0','0','0','0','0','0','0','0','0'],
    ['G','0','0','0','0','0','0','0','0','0','0'],
    ['H','0','0','0','0','0','0','0','0','0','0'],
    ['I','0','0','0','0','0','0','0','0','0','0'],
    ['J','0','0','0','0','0','0','0','0','0','0'],
    ]

def criar_matriz_back(): # <-- isso aqui é gambiarra pra fazer o 10x10 com feedback pro usuario

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

def inserir_na_matriz(matriz, linha, coluna, caractere):
    matriz[linha][coluna] = caractere

def verificar_posicao(matriz, linha, coluna):
    if matriz[linha][coluna] != '0':
        print("Local já ocupado!")

def posicionar_barco_hor(matriz,linha,coluna,tamanho):
        
        podePosicionar = True

        for i in range(tamanho):
            if matriz[linha][coluna] > matriz[linha][10] or matriz[linha+i][coluna+i] == -1: # se ele sair do tabuleiro, ou bater num barco(-1), ele seta podePosicionar como falso
                podePosicionar = False

        if podePosicionar: # preenche as devidas posicoes com o barco
            for i in range(tamanho):
                matriz[linha][coluna+i] = -1
        else:
            print("O seu barco está saindo do tabuleiro ou colidindo com outro barco! Escolha uma posição válida!")
            input_coord()

def print_info_barco(nome, tamanho):
    print(f"Você está posicionando o {nome}, ele possui TAMANHO {tamanho}")

def posicionar_porta():

    barco = "PORTA-AVIÕES"
    tamanho = 5
    eixo = -1
    linha = -1
    coluna = -1

    print_info_barco(barco,tamanho) 

    print("Escolha o eixo para posicionar o barco: ")
    print("[HORIZONTAL] ou [x] | [VERTICAL] ou [y]\n")

    while eixo == -1:
        eixo = input("Escolha o eixo: ").lower()
        eixo = converter_eixo(eixo)

    print_matriz(matrizJogadorBack)

    linha, coluna = input_coord()

    if eixo == "x": # ARRUMA ESSA BAGAÇA DESSE LOOP QUE TA HORRIVEL NAO TA FUNCINOANDO TO FAZENDO FAZ UMA HORA EU QUERO DORMIR E TEM COISA MAIS IMPORTANTE PRA FAZER

        posicionar_barco_hor(matrizJogadorBack,linha,coluna,tamanho)
            
                
    # elif eixo == "y":
    #     pass
                


def inicio_jogo():

    posicionar_porta()

    print_matriz(matrizJogadorBack)
    
    print("")

    linha = input("Digite a linha (caractere) aqui: ").strip().lower()
    linha = converter_caractere(linha)
    coluna = int(input("Digite a coluna (NUMERO) aqui: ")) # FAZER TRATAMENTO DE ERRO SE ELE ESCOLHER ALGO INVÁLIDO (FORA DO RANGE OU caractere)

    verificar_posicao(matrizJogadorBack, linha, coluna)
    
    inserir_na_matriz(matrizJogadorFront, linha, coluna, '🟩')
    inserir_na_matriz(matrizJogadorBack, linha, coluna, '1')
    print_matriz(matrizJogadorFront)

inicio_jogo()
inicio_jogo()