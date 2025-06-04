# humano x compuador
# Cada jogador deve ter um tabuleiro (matriz) de tamanho 5x100 ou 100x100 que irá conter as informações
# das coordenadas de cada embarcação, também deverá ter outro tabuleiro (matriz vazia) de tamanho
# 5x100 ou 100x100 (um para o computador e outro para o jogador) que será exibido como feedback
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

def criar_11x11(): # <-- isso aqui é gambiarra pra fazer o 100x100 com feedback pro usuario

    return [
    ['XX','01','02','03','04','05','06','07','08','09','10'],
    ['01','00','00','00','00','00','00','00','00','00','00'],
    ['02','00','00','00','00','00','00','00','00','00','00'],
    ['03','00','00','00','00','00','00','00','00','00','00'],
    ['04','00','00','00','00','00','00','00','00','00','00'],
    ['05','00','00','00','00','00','00','00','00','00','00'],
    ['06','00','00','00','00','00','00','00','00','00','00'],
    ['07','00','00','00','00','00','00','00','00','00','00'],
    ['08','00','00','00','00','00','00','00','00','00','00'],
    ['09','00','00','00','00','00','00','00','00','00','00'],
    ['10','00','00','00','00','00','00','00','00','00','00'],
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

def inicio_jogo():
    
    print_matriz(matrizJogadorFront)

    print("Escreva ")

inicio_jogo()
