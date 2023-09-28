

class BuscadorEmLargura:


    def buscar(self, grafo, vertice):
        niveis = [] # cada indice eh um nivel (lista de lista e nao matriz)
        vertices = [vertice]
        vertices_visitados = [vertice]
        
        while len(vertices):
            # lista de todos os vizinhos de cada vertice da lista de vertices
            vizinhos = []
            for v in vertices:
                # filtra todos vertices ainda nao visitados que sao vizinhos dos vertices da lista de vertices
                novos_vertices = list(filter(lambda x: x not in vertices_visitados, grafo.vizinhos(v)))
                # adiciona na lista de vertices visitados esses novos vertices e na lista de vizinhos
                vertices_visitados.extend(novos_vertices)
                vizinhos.extend(novos_vertices)

            # adiciona mais um nível e atualiza os a lista de vertices para agora ser a lista de vizinhos dos vertices
            niveis.append(vertices[:])
            vertices = vizinhos[:]

        # retorna os niveis
        return niveis[:]
            