# 3 - Contagem regressiva recursiva
def contagem_regressiva(n):
    # caso base: quando n é menor que 0, para a recursão
    if n < 0:
        return print("Lista vazia!")
    
    # imprime o número atual
    print(n)
    
    # chamada recursiva diminuindo o valor
    return contagem_regressiva(n - 1)


# entrada do usuário
numero = int(input("Digite um número positivo inteiro para a contagem regressiva: "))

# mensagem inicial
print(f"Contagem regressiva a partir de {numero}:")

# inicia a contagem
contagem_regressiva(numero)