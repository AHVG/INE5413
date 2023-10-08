import copy

class FortementeConexas:
    # Todas listas tem um elmento inutil, o primeiro, para não ficar colocando - 1 ou + 1 nos indices

    def __init__(self):
        self.tempo = 0 # Passar por parâmetro não funciona, pois é uma copia (GAMBIARRA)


    def converter_para_componentes(self, A):
        # Converte o vetor A em uma lista com cada uma das componentes fortemente ligadas do grafo
        casas_iniciais = {}
        
        for i, v in enumerate(A[1:]):
            if v is None:
                casas_iniciais[i + 1] = []
        
        for v_analisado, v_anterior in enumerate(A[1:]):
            v_analisado += 1
            v_atual = v_analisado
            while True:
                if v_anterior is None:
                    casas_iniciais[v_atual].append(v_analisado)
                    break
                v_atual, v_anterior = v_anterior, A[v_atual]

        componentes = []

        for ilha in casas_iniciais.keys():
            componentes.append(", ".join([str(i) for i in casas_iniciais[ilha]]))

        return copy.deepcopy(componentes)


    def buscarPorComponentes(self, grafo):
        C, T, A, F = self.DFS(grafo)

        grafo_transposto = grafo.obterTransposto() # O bom seria uma fabrica para criar grafos

        C_transposto, T_transposto, A_transposto, F_transposto = self.DFS_adaptado(grafo_transposto, F)

        return self.converter_para_componentes(A_transposto)


    def DFS(self, grafo):
        C = [False          for _ in range(grafo.qtdVertices() + 1)]
        T = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)]
        F = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)]        
        A = [None           for _ in range(grafo.qtdVertices() + 1)]

        self.tempo = 0

        for v in range(1, grafo.qtdVertices() + 1):
            if not C[v]:
                self.DFS_visit(grafo, v, C, T, A, F)

        return C, T, A, F


    def DFS_adaptado(self, grafo, F_linha):
        C = [False          for _ in range(grafo.qtdVertices() + 1)]
        T = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)]
        F = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)]        
        A = [None           for _ in range(grafo.qtdVertices() + 1)]

        self.tempo = 0
        vertices_ordenados = sorted(zip(list(range(1, grafo.qtdVertices() + 1)), F_linha[1:]), key=lambda x: x[1], reverse=True)

        for v, _ in vertices_ordenados:
            if not C[v]:
                self.DFS_visit(grafo, v, C, T, A, F)

        return C, T, A, F


    def DFS_visit(self, grafo, v, C, T, A, F):
        C[v] = True
        self.tempo += 1
        T[v] = self.tempo

        for u in grafo.vizinhos(v):
            if not C[u]:
                A[u] = v
                self.DFS_visit(grafo, u, C, T, A, F)

        self.tempo += 1
        F[v] = self.tempo
