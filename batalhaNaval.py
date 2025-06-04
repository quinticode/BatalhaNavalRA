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

import random
# conversão de letra para numero, coordenadas das linhas
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10


def criar_11x11(): # <-- isso aqui é gambiarra pra fazer o 10x10 com feedback pro usuario

    return [
    ['X','1','2','3','4','5','6','7','8','9','10'],
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
    matriz[linha][coluna].pop()
    matriz[linha][coluna]
    pass


def inicio_jogo():

    print_matriz(matrizJogadorFront)

    print("Selecione as coordenadas com LINHAS (horizontal) e COLUNAS (vertical), para posicionar a embarcação: ")

    linha = input("Digite a linha (LETRA) aqui: ").strip().lower()
    coluna = int(input("Digite a coluna (NUMERO) aqui: ")) # FAZER TRATAMENTO DE ERRO SE ELE ESCOLHER ALGO INVÁLIDO (FORA DO RANGE OU LETRA)

inicio_jogo()
