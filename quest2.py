# 2 - Soma dos elementos de um vetor com recursão
def soma_vetor(lista):
    # caso base: se a lista estiver vazia, retorna 0
    if len(lista) == 0:
        return 0
    
    
    # pega o primeiro elemento + soma do resto da lista
    return lista[0] + soma_vetor(lista[1:])


# vetor de exemplo
vetor = [4, 7, 2, 9]

# imprime o resultado da soma
print(f"A soma dos elementos do vetor {vetor} é {soma_vetor(vetor)}")