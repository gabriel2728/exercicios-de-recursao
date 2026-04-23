# -  Contagem de caminhos em um tabuleiro de entrega por drone
def contar_caminhos(n, m, i=0, j=0):
    # chegou no destino
    if i == n - 1 and j == m - 1:
        return 1
    
    # saiu da grade
    if i >= n or j >= m:
        return 0
    
    # recursão: baixo + direita
    return contar_caminhos(n, m, i + 1, j) + contar_caminhos(n, m, i, j + 1)

print(contar_caminhos(2, 2))