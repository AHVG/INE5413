

class Grafo:


    def __init__(self):
        self.__rotulos = [] # Não sei para que serve esses rotulos
        self.__matriz_de_adjacencia = []

    def qtdVertices(self):
        return len(self.__matriz_de_adjacencia)

    def qtdArestas(self):
        return sum([sum([1 for v in linha[i:] if v != float("Inf")]) for i, linha in enumerate(self.__matriz_de_adjacencia)])

    def grau(self, v):
        return sum(filter(lambda x: x != float("Inf"), self.__matriz_de_adjacencia[v - 1]))

    def rotulo(self, v): # Não sei que porra é esta
        return self.__rotulos[v - 1]

    def vizinhos(self, v):
        return [i + 1 for i, x in enumerate(self.__matriz_de_adjacencia[v - 1]) if x != float("Inf")]

    def haAresta(self, u, v):
        return self.__matriz_de_adjacencia[u - 1][v - 1] != float("Inf")

    def peso(self, u, v):
        return self.__matriz_de_adjacencia[u - 1][v - 1]

    def ler(self, arquivo):
        # TODO: É possível fazer bem melhor que isso
        with open(arquivo, "r") as arq:
            linhas = arq.read().split("\n")
        numero_de_vertices = int(linhas[0].split()[1])
        inicio_leitura_de_vertices = 1
        inicio_leitura_de_edges = numero_de_vertices + 2

        rotulos = linhas[inicio_leitura_de_vertices:inicio_leitura_de_edges - 1]
        self.__rotulos = [rotulo for v, rotulo in map(lambda x: x.split(), rotulos)]
        
        vertices = linhas[inicio_leitura_de_edges:]
        self.__matriz_de_adjacencia = [[float("Inf") for __ in range(numero_de_vertices)] for _ in range(numero_de_vertices)]
        for v, u, p in map(lambda x: map(float, x.split()), vertices):
            u = int(u) - 1
            v = int(v) - 1
            self.__matriz_de_adjacencia[v][u] = p
            self.__matriz_de_adjacencia[u][v] = p

    def __str__(self):
        return str(self.__matriz_de_adjacencia)
