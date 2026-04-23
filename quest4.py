# 4 - Potência de um número
def potencia(base, expoente):
    # caso base
    if expoente == 0:
        return 1
    
    # expoente negativo
    if expoente < 0:
        return 1 / potencia(base, -expoente)
    
    # recursão normal
    return base * potencia(base, expoente - 1)

# Pede ao usuário para inserir a base
base = int(input("Digite a base:"))

# Pede ao usuário para inserir o expoente
expoente = int(input("Digite o expoente:"))
print(potencia(base, expoente))   
print(potencia(base, -expoente))  