from grafo import Grafo


class FloydWarshall:

    def funcao_w(self, grafo: Grafo) -> list[list]:
        # define uma matriz D, que ira conter as distancias entre todos pares de vertices em apenas 1 transicao
        D = []
        # itera por todos pares de vertices possiveis
        for u in range(grafo.qtdVertices()):
            linha = []
            for v in range(grafo.qtdVertices()):
                # a distancia de um vertice para ele mesmo eh 0
                if u == v:
                    linha.append(0)
                # se ha uma aresta u<->v adiciona seu peso 
                elif grafo.haAresta(u+1, v+1):
                    linha.append(grafo.peso(u+1, v+1))
                # se nao ha conexao direta entre os vertices, sua distancia inicial eh infinita
                else:
                    linha.append(grafo.sem_aresta)
            D.append(linha)
        return D

    def calcular(self, grafo: Grafo) -> list[list]:
        # define D(0) como a funcao W
        D_anterior = self.funcao_w(grafo)
        # itera por todos os vertices intermediarios do relaxamento
        for k in range(grafo.qtdVertices()):
            # cria um D(n) vazio
            D_atual = [[] for i in range(grafo.qtdVertices())]
            # itera por todos os pares de vertices
            for u in range(grafo.qtdVertices()):
                for v in range(grafo.qtdVertices()):
                    # aplica o relaxamento entre eles
                    # minimo entre a distancia atual e u->k->v
                    D_atual[u].append(min(D_anterior[u][v], D_anterior[u][k] + D_anterior[k][v]))
            # define o D(n-1) como D(n) para fazer a proxima iteracao
            D_anterior = D_atual
        return D_atual