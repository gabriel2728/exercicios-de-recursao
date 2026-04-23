# 7- Exploração de salas em um mapa inteligente

def explorar_salas(mapa, sala, visitadas=None):
    if visitadas is None:
        visitadas = set()
    
    # evita repetir sala
    if sala in visitadas:
        return
    
    # marca como visitada
    visitadas.add(sala)
    
    # mostra a sala
    print(sala)
    
    # visita as próximas salas
    for proxima in mapa[sala]:
        explorar_salas(mapa, proxima, visitadas)

mapa = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

# Inicia a exploração a partir da sala "B"
explorar_salas(mapa, "A")

