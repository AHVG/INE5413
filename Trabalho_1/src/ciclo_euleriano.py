from grafo import Grafo

class CicloEuleriano:
    def isEulerian(self, grafo: Grafo) -> bool:
        # Verifica se o grafo é euleriano
        for v in range(1, grafo.qtdVertices() + 1):
            if grafo.grau(v) % 2 != 0:
                return False
        return True
    
    def EulerianTour(self, grafo: Grafo, vertice: int) -> list:
        if not self.isEulerian(grafo):
            return None
        ciclo = []
        vertice_atual = vertice 

        while True:
            vizinhos = grafo.vizinhos(vertice_atual)
            if not vizinhos:
                break  # Não há mais arestas disponíveis para este vértice
            proximo_vertice = vizinhos[0]
            grafo.removerAresta(vertice_atual, proximo_vertice)  # Marque a aresta como visitada
            ciclo.append((vertice_atual, proximo_vertice))
            vertice_atual = proximo_vertice

        return ciclo
