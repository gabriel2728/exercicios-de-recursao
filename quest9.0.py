# 9- Decodificador de mensagens fragmentadas
#  Desafio extra

def decodificar_completo(s):
    # cria um conjunto para guardar strings já visitadas

    visitados = set()
    
    def rec(s):
        # se essa string já foi processada, para aqui
        if s in visitados:
            return
        
        # marca como visitada
        visitados.add(s)
        
        # imprime a string atual
        print(s)
        
        # caso base: quando só sobra 1 caractere
        if len(s) == 1:
            return
        
        # percorre cada posição da string
        for i in range(len(s)):
            # cria uma nova string removendo o caractere da posição i
            nova = s[:i] + s[i+1:]
            
            # chama a função recursivamente com a nova string
            rec(nova)
    
    # inicia a recursão com a string original
    rec(s)



decodificar_completo("abc")