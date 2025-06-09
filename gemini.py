import random
import os
import time

# --- Constantes do Jogo ---
TAMANHO_TABULEIRO = 10
AGUA = '🌊'
NAVIO = '🚢'
ACERTO = '💥'
ERRO = '🌀'
NAVIO_AFUNDADO_ICONE = '☠️'

EMBARCACOES = [
    ("Porta-aviões", 5),
    ("Navio-tanque", 4),
    ("Contratorpedeiro", 3),
    ("Submarino", 2),
    ("Destroier", 1)
]

# --- Funções do Jogo ---

def criar_tabuleiro():
    """Cria e retorna um tabuleiro 10x10 vazio (preenchido com 'água')."""
    return [[AGUA for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]

def exibir_tabuleiros(tabuleiro_jogador, tabuleiro_computador, vida_barcos_jogador, vida_barcos_computador):
    """Exibe ambos os tabuleiros e a contagem de embarcações restantes."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("================ BATALHA NAVAL ================")
    
    # Contagem de barcos restantes
    barcos_restantes_comp = sum(1 for vida in vida_barcos_computador.values() if vida > 0)
    barcos_restantes_jog = sum(1 for vida in vida_barcos_jogador.values() if vida > 0)

    print(f"\n--- TABULEIRO DO COMPUTADOR (Embarcações restantes: {barcos_restantes_comp}) ---")
    print("   " + "  ".join([str(i+1) for i in range(TAMANHO_TABULEIRO)]))#indice numerico
    for i, linha in enumerate(tabuleiro_computador):
        print(f"{chr(ord('A') + i)}  {'  '.join(linha)}")

    print(f"\n--- SEU TABULEIRO (Embarcações restantes: {barcos_restantes_jog}) ---")
    print("   " + "  ".join([str(i+1) for i in range(TAMANHO_TABULEIRO)]))
    for i, linha in enumerate(tabuleiro_jogador):
        # Exibe os navios no tabuleiro do jogador
        linha_visivel = [NAVIO if celula == NAVIO else celula for celula in tabuleiro_jogador[i]]
        print(f"{chr(ord('A') + i)}  {'  '.join(linha_visivel)}")
    print("==============================================")


def obter_coordenadas_jogador():
    """Pede e valida as coordenadas (linha e coluna) do jogador."""
    letras_validas = "ABCDEFGHIJ"
    while True:
        try:
            coord = input("Digite a coordenada para o ataque (ex: A5): ").upper().strip()
            letra, numero = coord[0], coord[1:]
            
            if letra in letras_validas and numero.isdigit():
                linha = letras_validas.find(letra)
                coluna = int(numero) - 1
                if 0 <= coluna < TAMANHO_TABULEIRO:
                    return linha, coluna
            print("Coordenada inválida! Use o formato LetraNúmero (ex: A5, B10).")
        except (ValueError, IndexError):
            print("Formato de entrada inválido. Tente novamente.")


def validar_posicao(tabuleiro, linha, coluna, tamanho, orientacao):
    """Verifica se uma embarcação pode ser posicionada no local desejado."""
    if orientacao == 'h': # Horizontal
        if coluna + tamanho > TAMANHO_TABULEIRO:
            return False
        return all(tabuleiro[linha][coluna+i] == AGUA for i in range(tamanho))
    else: # Vertical
        if linha + tamanho > TAMANHO_TABULEIRO:
            return False
        return all(tabuleiro[linha+i][coluna] == AGUA for i in range(tamanho))

def posicionar_embarcacao(tabuleiro, linha, coluna, tamanho, orientacao, id_barco):
    """Posiciona uma embarcação no tabuleiro, marcando com seu ID."""
    if orientacao == 'h':
        for i in range(tamanho):
            tabuleiro[linha][coluna+i] = id_barco
    else:
        for i in range(tamanho):
            tabuleiro[linha+i][coluna] = id_barco

def setup_jogador(tabuleiro_secreto):
    """Permite que o jogador posicione suas embarcações."""
    tabuleiro_visivel = criar_tabuleiro()
    for nome, tamanho in EMBARCACOES:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- Posicione suas embarcações ---")
            exibir_tabuleiros(criar_tabuleiro(), tabuleiro_visivel, {}, {}) # Mostra o tabuleiro do jogador
            
            print(f"\nPosicionando: {nome} (tamanho {tamanho})")
            orientacao = input("Orientação ('h' para horizontal, 'v' para vertical): ").lower()
            if orientacao not in ['h', 'v']:
                print("Orientação inválida. Tente novamente.")
                time.sleep(1)
                continue
            
            try:
                coord = input(f"Digite a coordenada inicial (ex: A1): ").upper()
                letra, numero = coord[0], coord[1:]
                linha = ord(letra) - ord('A')
                coluna = int(numero) - 1

                if validar_posicao(tabuleiro_secreto, linha, coluna, tamanho, orientacao):
                    posicionar_embarcacao(tabuleiro_secreto, linha, coluna, tamanho, orientacao, nome)
                    posicionar_embarcacao(tabuleiro_visivel, linha, coluna, tamanho, orientacao, NAVIO)
                    break
                else:
                    print("Posição inválida! Embarcação fora do tabuleiro ou sobrepondo outra.")
                    time.sleep(2)
            except (ValueError, IndexError):
                print("Coordenada inválida. Tente novamente.")
                time.sleep(2)

def setup_computador(tabuleiro_secreto):
    """Posiciona as embarcações do computador aleatoriamente."""
    for nome, tamanho in EMBARCACOES:
        while True:
            orientacao = random.choice(['h', 'v'])
            linha = random.randint(0, TAMANHO_TABULEIRO - 1)
            coluna = random.randint(0, TAMANHO_TABULEIRO - 1)

            if validar_posicao(tabuleiro_secreto, linha, coluna, tamanho, orientacao):
                posicionar_embarcacao(tabuleiro_secreto, linha, coluna, tamanho, orientacao, nome)
                break

def realizar_ataque(atacante, tabuleiro_visivel, tabuleiro_secreto, vida_barcos, cooldown_tiros):
    """Processa a jogada de um atacante (Jogador ou Computador)."""
    if atacante == "Jogador":
        while True:
            linha, coluna = obter_coordenadas_jogador()
            if (linha, coluna) not in cooldown_tiros:
                cooldown_tiros.add((linha, coluna))
                break
            else:
                print("Você já atirou aí. Escolha outra coordenada.")
    else: # Computador
        while True:
            linha = random.randint(0, TAMANHO_TABULEIRO - 1)
            coluna = random.randint(0, TAMANHO_TABULEIRO - 1)
            if (linha, coluna) not in cooldown_tiros:
                cooldown_tiros.add((linha, coluna))
                print(f"\nComputador ataca na coordenada {chr(ord('A') + linha)}{coluna + 1}...")
                time.sleep(1)
                break

    id_barco_atingido = tabuleiro_secreto[linha][coluna]
    if id_barco_atingido != AGUA:
        tabuleiro_visivel[linha][coluna] = ACERTO
        vida_barcos[id_barco_atingido] -= 1
        print(f"{atacante} acertou um alvo! {ACERTO}")

        if vida_barcos[id_barco_atingido] == 0:
            print(f"O {id_barco_atingido} do oponente foi afundado! {NAVIO_AFUNDADO_ICONE}")
        
        return True # Acerto
    else:
        tabuleiro_visivel[linha][coluna] = ERRO
        print(f"{atacante} errou o tiro! {ERRO}")
        return False # Erro

# --- Fluxo Principal do Jogo ---
def jogar():
    """Função principal que executa o jogo Batalha Naval."""
    # Tabuleiros "secretos" que guardam a posição real dos barcos
    tabuleiro_secreto_jogador = criar_tabuleiro()
    tabuleiro_secreto_computador = criar_tabuleiro()
    
    # Tabuleiros "visíveis" que mostram os resultados dos ataques
    tabuleiro_visivel_jogador = criar_tabuleiro()
    tabuleiro_visivel_computador = criar_tabuleiro()

    # Estrutura para guardar a vida de cada barco
    vida_barcos_jogador = {nome: tamanho for nome, tamanho in EMBARCACOES}
    vida_barcos_computador = {nome: tamanho for nome, tamanho in EMBARCACOES}
    
    # Guarda as coordenadas já atacadas para evitar repetição
    tiros_do_jogador = set()
    tiros_do_computador = set()

    # Fase de posicionamento
    setup_jogador(tabuleiro_secreto_jogador)
    setup_computador(tabuleiro_secreto_computador)

    # Loop principal do jogo
    while True:
        exibir_tabuleiros(tabuleiro_visivel_jogador, tabuleiro_visivel_computador, vida_barcos_jogador, vida_barcos_computador)
        
        # Turno do Jogador
        print("\n--- SEU TURNO ---")
        realizar_ataque("Jogador", tabuleiro_visivel_computador, tabuleiro_secreto_computador, vida_barcos_computador, tiros_do_jogador)
        if all(vida == 0 for vida in vida_barcos_computador.values()):
            print("\nPARABÉNS! Você venceu a batalha!")
            break
        
        input("Pressione Enter para o turno do computador...")

        # Turno do Computador
        realizar_ataque("Computador", tabuleiro_visivel_jogador, tabuleiro_secreto_jogador, vida_barcos_jogador, tiros_do_computador)
        exibir_tabuleiros(tabuleiro_visivel_jogador, tabuleiro_visivel_computador, vida_barcos_jogador, vida_barcos_computador)
        if all(vida == 0 for vida in vida_barcos_jogador.values()):
            print("\nFIM DE JOGO! O computador venceu.")
            break

        input("Pressione Enter para continuar...")

    print("\nJogo desenvolvido por: Luis Felipe, Davi Cagnato e Larissa Adames.")
    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()