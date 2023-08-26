

class Grafo:


    def __init__(self, grafo_em_matriz):
        self.__matriz_de_adjacencia = grafo_em_matriz[:]

    def qtdVertices(self):
        return len(self.__matriz_de_adjacencia)

    def qtdArestas(self):
        return sum([sum([1 for v in linha[i:] if v != float("Inf")]) for i, linha in enumerate(self.__matriz_de_adjacencia)])

    def grau(self, v):
        return sum(filter(lambda x: x != float("Inf"), self.__matriz_de_adjacencia[v]))

    def rotulo(self, v): # Não sei que porra é esta
        pass

    def vizinhos(self, v):
        return [i for i, x in enumerate(self.__matriz_de_adjacencia[v]) if x != float("Inf")]

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
print(g.grau(1))
print(g.vizinhos(0))
print(g.vizinhos(1))
print(g.vizinhos(2))