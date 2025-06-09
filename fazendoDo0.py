import random 
import os

## constantes
tabuleiro = 10
agua = "🌊"
navio = "🚢"
acerto = "💥"
erro = "🌀"
navioAfundado = "☠️"

embarcacoes = [
    ("Porta-aviões", 5),
    ("Navio-tanque", 4),
    ("Contratorpedeiro", 3),
    ("Submarino", 2),
    ("Destroier", 1)
]


#funcoes
def criarTabuleiro():
    return [[agua for i in range(tabuleiro)] for i in range(tabuleiro)] #matriz tabaleiro

def exibirTabuleiros(tabJogador, tabComputador, vidaBarcosJogador, vidaBarcosComp):
    os.system("cls" if os.name == "nt" else "clear") #limpar terminal win ou linux

    print("---------Batalha Naval---------")