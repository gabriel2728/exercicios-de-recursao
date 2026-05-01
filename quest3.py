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


# DESAFIO EXTRA
print("Desafio extra: contagem progressiva recursiva")
def contagem_progressiva(atual, n):
    
    # caso base: quando passa do limite, para a recursão
    if atual > n:
        return
    
    # imprime o número atual
    print(atual)
    
    # chamada recursiva:
    # aumenta o valor atual em 1
    contagem_progressiva(atual + 1, n)


# pede um número ao usuário
numero = int(input("Digite um número positivo inteiro: "))

# mensagem inicial
print(f"Contagem até {numero}:")

# inicia a contagem a partir do 0
contagem_progressiva(0, numero)