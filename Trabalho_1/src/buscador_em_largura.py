

class BuscadorEmLargura:

    def buscar(self, grafo, vertice):
        niveis = [] # Cada indice é um nivel (lista de lista e não matriz)
        vertices_a_serem_visitados_por_nivel = [vertice]
        vertices_visitados = [vertice]
        nivel = 1
        while len(vertices_a_serem_visitados_por_nivel):
            vertices = vertices_a_serem_visitados_por_nivel[:]
            vizinhos_por_nivel = []
            for v in vertices:
                vizinhos_por_nivel.extend(grafo.vizinhos(v))

            vertices_a_serem_adicionados = [x for x in vizinhos_por_nivel if x not in vertices_visitados]

            vertices_visitados.extend(vertices_a_serem_adicionados[:])
            vertices_a_serem_visitados_por_nivel = vertices_a_serem_adicionados[:]
            niveis.append(vertices[:])
            nivel += 1
        return niveis
            