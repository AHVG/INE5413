

class BuscadorEmLargura:


    def buscar(self, grafo, vertice):
        niveis = [] # Cada indice é um nivel (lista de lista e não matriz)
        vertices = [vertice]
        vertices_visitados = [vertice]
        
        while len(vertices):
            vizinhos = []
            for v in vertices:
                novos_vertices = list(filter(lambda x: x not in vertices_visitados, grafo.vizinhos(v)))
                vertices_visitados.extend(novos_vertices)
                vizinhos.extend(novos_vertices)

            vertices_visitados.extend(vizinhos[:])
            niveis.append(vertices[:])
            vertices = vizinhos[:]

        return niveis[:]
            