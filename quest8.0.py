# -  Contagem de caminhos em um tabuleiro de entrega por drone
# - Desafio extra (com bloqueios)

def contar_caminhos(matriz, i=0, j=0):
    n = len(matriz)
    m = len(matriz[0])
    
    # fora da grade
    if i >= n or j >= m:
        return 0
    
    # célula bloqueada
    if matriz[i][j] == 1:
        return 0
    
    # chegou no destino
    if i == n - 1 and j == m - 1:
        return 1
    
    return contar_caminhos(matriz, i + 1, j) + contar_caminhos(matriz, i, j + 1)

grade = [
    [0, 0],
    [1, 0]
]

print(contar_caminhos(grade))