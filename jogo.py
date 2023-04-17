# declara as constantes com nmr de linhas e colunas
NUM_LINHAS = 6
NUM_COLUNAS = 7

#mastriz do jogo
jogo = []

# cria uma matriz com o nmr de linhas e colunas inicialmente vazios
# atribui um " " para cada posição
def cria_jogo():
    for i in range(NUM_LINHAS):
        jogo.append([])
        for _ in range(NUM_COLUNAS):
            jogo[i].append(' ')

def mostra_jogo():
    print()
    for i,linha in enumerate(jogo, start=1):
        print(f'{i} |', end = "")
        for casa in linha:
         print(f' {casa} ', end ="")
        print("|")
    print('  +---------------------+')
    print("    1  2  3  4  5  6  7")

def linha_disponivel(coluna):
    disponivel = -1
    # for decresente
    for i in range(NUM_LINHAS - 1, -1,-1):
        if jogo[i][coluna] == ' ':
            disponivel = i
            break
    return disponivel

def vencedor(simbolo):
    # quatro colunas sequenciais na mesma linha (horizontal)
    for l in range(NUM_LINHAS):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c] == simbolo and jogo[l][c + 1] == simbolo and jogo[l][c + 2] == simbolo and jogo[l][c + 3] == simbolo:
             return True
    
    # quatro linhas sequenciais na mesma coluna (vertical)
    for l in range(NUM_LINHAS - 3):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c] == simbolo and jogo[l + 1][c] == simbolo and jogo[l + 2][c] == simbolo and jogo[l + 3][c] == simbolo:
             return True
            
    # quatro linhas sequenciais na transversal(transversal para baixo ou esquerda para direita)
    for l in range(NUM_LINHAS - 3):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c] == simbolo and jogo[l + 1][c + 1] == simbolo and jogo[l + 2][c + 2] == simbolo and jogo[l + 3][c + 3] == simbolo:
             return True
            
    # quatro linhas sequenciais na transversal(transversal para cima ou direita para esquerda)      
    for l in range(NUM_LINHAS - 1, NUM_LINHAS - 3, -1):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c] == simbolo and jogo[l - 1][c + 1] == simbolo and jogo[l - 2][c + 2] == simbolo and jogo[l - 3][c + 3] == simbolo:
             return True
    


# chama as funçoes iniciais
cria_jogo()
mostra_jogo()

print("\nJogo Connect 4")
print("="*40)
print("Informe o número da coluna(1..7) ou 0 para sair")

contador = 1 #serve para verificar se houve empate e quem joga

while True:
    #operador ternário em python
    jogador = "x" if contador % 2 == 1 else 'o'
    coluna = int(input(f"\nJogador '{jogador}', informe a coluna: "))

    if coluna == 0 or coluna > NUM_COLUNAS:
        break

    linha = linha_disponivel(coluna - 1)

    jogo[linha][coluna - 1]= jogador
    if linha == -1:
        print('Colna esta cheia...')
    else:
        jogo[linha][coluna - 1] = jogador
        contador += 1
    mostra_jogo()

    if vencedor(jogador):
        print()
        print('*'*40)
        print(f"Parabens Jogador '{jogador}' !! Voce é o vencedor")
        break

    if contador == NUM_LINHAS * NUM_COLUNAS:
        print()
        print('*'*40)
        print(f"Ah deu Empate")
        break



