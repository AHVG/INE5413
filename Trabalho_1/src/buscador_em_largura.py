

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
                novos_vertices = list(filter(lambda x: x not in vertices_visitados, grafo.vizinhos(v)))
                vertices_visitados.extend(novos_vertices)
                vizinhos_por_nivel.extend(novos_vertices)

            vertices_visitados.extend(vizinhos_por_nivel[:])
            vertices_a_serem_visitados_por_nivel = vizinhos_por_nivel[:]
            niveis.append(vertices[:])
            nivel += 1
        return niveis
            