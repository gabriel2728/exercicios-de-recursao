# 3 - Contagem progressiva recursiva
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