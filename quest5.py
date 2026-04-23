# 5 - Inverter uma string
def inverter_string(s):
    # caso base: string vazia → retorna ela mesma
    if len(s) == 0:
        return s
    
    # pega o último caractere + recursão do resto
    return s[-1] + inverter_string(s[:-1])


# entrada do usuário
texto = str(input("Digite uma string para inverter:"))

# imprime o resultado
print(f"A string invertida é: {inverter_string(texto)}")