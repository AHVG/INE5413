

class BuscadorEmLargura:


    def buscar(self, grafo, vertice):
        niveis = [] # Cada indice é um nivel (lista de lista e não matriz)
        vertices = [vertice]
        vertices_visitados = [vertice]
        
        while len(vertices):
            # Lista de todos os vizinhos de cada vertice da lista de vertices
            vizinhos = []
            for v in vertices:
                # filtra todos vertices ainda não visitados que são vizinhos dos vertices da lista de vertices
                novos_vertices = list(filter(lambda x: x not in vertices_visitados, grafo.vizinhos(v)))
                # adiciona na lista de vertices visitados esses novos vertices e na lista de vizinhos
                vertices_visitados.extend(novos_vertices)
                vizinhos.extend(novos_vertices)

            # Adiciona mais um nível e atualiza os a lista de vertices para agora ser a lista de vizinhos dos vertices
            niveis.append(vertices[:])
            vertices = vizinhos[:]

        # retorna os níveis
        return niveis[:]
            