from grafo import Grafo


class FloydWarshall:

    def funcao_w(self, grafo: Grafo) -> list[list]:
        D = []
        for u in range(grafo.qtdVertices()):
            linha = []
            for v in range(grafo.qtdVertices()):
                if u == v:
                    linha.append(0)
                elif grafo.haAresta(u+1, v+1):
                    linha.append(grafo.peso(u+1, v+1))
                else:
                    linha.append(grafo.sem_aresta)
            D.append(linha)
        return D

    def calcular(self, grafo: Grafo) -> list[list]:
        D_anterior = self.funcao_w(grafo)
        for k in range(grafo.qtdVertices()):
            D_atual = [[] for i in range(grafo.qtdVertices())]
            for u in range(grafo.qtdVertices()):
                for v in range(grafo.qtdVertices()):
                    D_atual[u].append(min(D_anterior[u][v], D_anterior[u][k] + D_anterior[k][v]))
            D_anterior = D_atual
        return D_atual
