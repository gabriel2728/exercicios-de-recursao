# 1 - Fatorial de um número com recursão
def fatorial(n):
    # caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    else:
        # passo recursivo:
        # n! = n * (n-1)!
        return n * fatorial(n - 1)



numero = int(input("Digite um número positivo inteiro para calcular o fatorial: "))

# 1 - Fatorial de um número com recursão
def fatorial(n):
    # caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    else:
        # passo recursivo:
        # n! = n * (n-1)!
        return n * fatorial(n - 1)


# pede um número ao usuário
numero = int(input("Digite um número positivo inteiro para calcular o fatorial: "))

# chama a função e mostra o resultado
print(f"O fatorial de {numero} é {fatorial(numero)}")
print(f"O fatorial de {numero} é {fatorial(numero)}")