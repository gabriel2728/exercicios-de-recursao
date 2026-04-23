# 9- Decodificador de mensagens fragmentadas
# Removendo pela direita
def decodificar_direita(s):
    # caso base
    if len(s) == 1:
        print(s)
        return
    
    print(s)
    
    # remove o último caractere
    decodificar_direita(s[:-1])

print("Decodificando pela direita:")
decodificar_direita("abc")

# Removendo pela esquerda
def decodificar_esquerda(s):
    if len(s) == 1:
        print(s)
        return
    
    print(s)
    
    # remove o primeiro caractere
    decodificar_esquerda(s[1:])

print("Decodificando pela esquerda:")
decodificar_esquerda("abc")