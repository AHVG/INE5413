

class Grafo:


    def __init__(self, grafo_em_matriz):
        self.__matriz_de_adjacencia = grafo_em_matriz[:]

    def qtdVertices(self):
        return len(self.__matriz_de_adjacencia)

    def qtdArestas(self):
        return sum([sum([1 for v in linha[i:] if v != float("Inf")]) for i, linha in enumerate(self.__matriz_de_adjacencia)])

    def grau(self, v):
        pass

    def rotulo(self, v):
        pass

    def vizinhos(self, v):
        pass

    def haAresta(self, u, v):
        pass

    def peso(self, u, v):
        pass

    def ler(self, arquivo):
        pass

    def __str__(self):
        return str(self.__matriz_de_adjacencia)

g = Grafo([
[float("Inf"), 1, 1],
[1, float("Inf"), float("Inf")],
[1, float("Inf"), float("Inf")]
])

print(g)
print(g.qtdArestas())