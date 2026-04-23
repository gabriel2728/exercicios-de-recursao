# 10- Sistema de recomendação em rede social universitária
rede = {
    "Renato": ["Ana", "Bruno"],
    "Ana": ["Carla"],
    "Bruno": ["Diego"],
    "Carla": [],
    "Diego": []
}

def explorar_rede(rede, pessoa, visitados=None):
    if visitados is None:
        visitados = set()
    
    # evita repetir
    if pessoa in visitados:
        return
    
    # marca como visitado
    visitados.add(pessoa)
    
    # mostra a pessoa
    print(pessoa)
    
    # visita conexões
    for amigo in rede[pessoa]:
        explorar_rede(rede, amigo, visitados)

explorar_rede(rede, "Renato")

print("\n" + 38 * '=')

# Desafio extra: contando o total de usuários na rede
def explorar_rede(rede, pessoa, visitados=None):
    if visitados is None:
        visitados = set()
    
    if pessoa in visitados:
        return 0
    
    visitados.add(pessoa)
    print(pessoa)
    
    total = 1  # conta a pessoa atual
    
    for amigo in rede[pessoa]:
        total += explorar_rede(rede, amigo, visitados)
    
    return total
print("Explorando a rede e contando usuários:")
total = explorar_rede(rede, "Renato")
print("Total de usuários:", total)