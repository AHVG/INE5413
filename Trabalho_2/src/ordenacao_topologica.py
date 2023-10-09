

class OrdenacaoTopologica:
    """
        Classe que obtêm a ordenação topologica de um grafo
    """
    
    def __init__(self):
        self.tempo = 0 # Passar por parâmetro não funciona, pois é uma copia
    
    def ordena(self, G):
        """
        Função que obtêm a ordenação topológica do vertice G

        @param: G grafo que será analisado

        @return: Ordenação topológica (vetor)
        """

        C = [False          for _ in range(G.qtdVertices())] # Todos os vertices não visitados
        T = [float("Inf")   for _ in range(G.qtdVertices())] # Tempo inicial infinito
        F = [float("Inf")   for _ in range(G.qtdVertices())] # Tempo final infinito
        O = []                                               # Ordenação topológica

        # Visita todas as componentes conexas
        for u in range(G.qtdVertices()):
            if not C[u]:
                self.DFS_visit_OT(G, u, C, T, F, O)

        return O

    def DFS_visit_OT(self, G, v, C, T, F, O):
        """
        Função que visita efetivamente um vertice

        @param: G grafo em que foi aplicado a ordenação topológica
        @param: v vertice atual
        @param: C vetor de visitados
        @param: T vetor do tempo inicial
        @param: F vetor de tempo final
        @param: O ordenação topológica

        """
        # Define o vertice atual como visitado e seu tempo inicial
        C[v] = True
        self.tempo += 1
        T[v] = self.tempo

        # Visita todos seus vizinhos ainda não visitados
        for _, u in G.obterArestasParaVizinhos(v):
            if not C[u-1]:
                self.DFS_visit_OT(G, u-1, C, T, F, O)

        # Define seu tempo final e insere no começo do vetor O o vertice v
        self.tempo += 1
        F[v] = self.tempo
        O.insert(0, v) 