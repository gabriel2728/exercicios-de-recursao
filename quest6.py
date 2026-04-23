# 6 - Sequência de Fibonacci

def fibonacci(n):
    # caso base 1:
    # o 0º número da sequência é 0
    if n == 0:
        return 0
    
    # caso base 2:
    # o 1º número da sequência é 1
    if n == 1:
        return 1
    
    # passo recursivo:
    # cada número é a soma dos dois anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)


# entrada do usuário
n = int(input("Digite um número para calcular a sequência de Fibonacci: "))

# imprime o resultado
print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")