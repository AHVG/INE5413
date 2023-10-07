

class FortementeConexas:


    def buscarPorComponentes(self, grafo):
        C, T, A, F = self.DFS(grafo)

        grafo_transposto = grafo.obterTransposto() # O bom seria uma fabrica para criar grafos
        
        C_transposto, T_transposto, A_transposto, F_transposto = self.DFS_adaptado(grafo_transposto, F)

        return A_transposto

    # TODO: Colocar numa classe esses DFS's
    def DFS(self, grafo):
        C = [False for _ in range(grafo.qtdVertices())]
        T = [float("Inf") for _ in range(grafo.qtdVertices())]
        F = [float("Inf") for _ in range(grafo.qtdVertices())]        
        A = [None for _ in range(grafo.qtdVertices())]

        tempo = 0
        for v in range(1, grafo.qtdVertices() + 1):
            if not C[v - 1]:
                self.DFS_visit(grafo, v, C, T, A, F, tempo)

        return C, T, A, F


    def DFS_adaptado(self, grafo, F):
        C = [False for _ in range(grafo.qtdVertices())]
        T = [float("Inf") for _ in range(grafo.qtdVertices())]
        F = [float("Inf") for _ in range(grafo.qtdVertices())]        
        A = [None for _ in range(grafo.qtdVertices())]

        tempo = 0
        vertices_ordenados = sorted(zip(list(range(1, grafo.qtdVertices() + 1)), F), lambda x: x[1])
        for v, _ in vertices_ordenados:
            if not C[v - 1]:
                self.DFS_visit(grafo, v, C, T, A, F, tempo)

        return C, T, A, F


    def DFS_visit(self, grafo, v, C, T, A, F):
        C[v - 1] = True
        tempo += 1
        T[v - 1] = tempo
        for u in grafo.vizinhos(v):
            if not C[u - 1]:
                A[u - 1] = v
                self.DFS_visit(grafo, u, C, T, A, F, tempo)
        tempo += 1
        F[v - 1] = tempo
