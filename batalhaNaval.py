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

# conversão de letra para numero, coordenadas das linhas
def converter_letra(letra):
    if letra == "a" or letra == "1":
        return 1
    elif letra == "b" or letra == "2":
        return 2
    elif letra == "c" or letra == "3":
        return 3
    elif letra == "d" or letra == "4":
        return 4
    elif letra == "e" or letra == "5":
        return 5
    elif letra == "f" or letra == "6":
        return 6
    elif letra == "g" or letra == "7":
        return 7
    elif letra == "h" or letra == "8":
        return 8
    elif letra == "i" or letra == "9":
        return 9
    elif letra == "j" or letra == "10":
        return 10

def converter_eixo(eixo):
    if eixo == "horizontal" or eixo == "x":
        return "x"
    elif eixo == "vertical" or eixo == "y":
        return "y"
    else:
        print("Digite um valor válido!")
        return -1

def criar_11x11(): # <-- isso aqui é gambiarra pra fazer o 10x10 com feedback pro usuario

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
    
def print_matriz(matriz):

    print()

    for i in range(len(matriz)):
        print(matriz[i])

    print()

matrizJogadorFront = criar_11x11() 
matrizJogadorBack = criar_11x11()
matrizComputadorFront = criar_11x11()
matrizComputadorBack = criar_11x11()

def inserir_na_matriz(matriz, linha, coluna, caractere):
    matriz[linha][coluna] = caractere

def verificar_posicao(matriz, linha, coluna):
    if matriz[linha][coluna] != '0':
        print("Local já ocupado!")

def print_info_barco(nome, tamanho):
    print(f"Você está posicionando o {nome}, ele possui TAMANHO {tamanho}")

def posicionar_porta():

    barco = "PORTA-AVIÕES"
    tamanho = 5
    eixo = -1

    print_info_barco(barco,tamanho) 

    print("Escolha o eixo para posicionar o barco: ")
    print("[HORIZONTAL] ou [x] | [VERTICAL] ou [y]\n")

    while eixo == -1:
        eixo = input("Escolha o eixo: ").lower()
        eixo = converter_eixo(eixo)

    print_matriz(matrizJogadorFront)

    if eixo == "x":
        print(f"Você escolheu o eixo HORIZONTAL, o {barco} se estenderá 5 CASAS da ESQUERDA para a DIREITA")
    elif eixo == "y":
        print(f"Você escolheu o eixo VERTICAL, o {barco} se estenderá 5 CASAS de CIMA para BAIXO")
    
    
    print("")
    linha = input("Digite a linha (LETRA) da posição aqui: ").strip().lower()
    linha = converter_letra(linha)
    coluna = int(input("Digite a coluna (NUMERO) da posição aqui: ")) # FAZER TRATAMENTO DE ERRO SE ELE ESCOLHER ALGO INVÁLIDO (FORA DO RANGE OU LETRA)


def inicio_jogo():

    posicionar_porta()

    print_matriz(matrizJogadorFront)
    
    print("")

    linha = input("Digite a linha (LETRA) aqui: ").strip().lower()
    linha = converter_letra(linha)
    coluna = int(input("Digite a coluna (NUMERO) aqui: ")) # FAZER TRATAMENTO DE ERRO SE ELE ESCOLHER ALGO INVÁLIDO (FORA DO RANGE OU LETRA)

    verificar_posicao(matrizJogadorBack, linha, coluna)
    
    inserir_na_matriz(matrizJogadorFront, linha, coluna, '🟩')
    inserir_na_matriz(matrizJogadorBack, linha, coluna, '1')
    print_matriz(matrizJogadorFront)

inicio_jogo()
inicio_jogo()