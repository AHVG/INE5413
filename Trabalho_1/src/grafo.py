import copy

class Grafo:


    sem_aresta = float("Inf") # Pode ser qualquer outro valor mágico, mas foi escolhido infinito pq é o mais descritivo


    def __init__(self, _ehDirigido: bool, _ehPonderado: bool):
        self.ehDirigido = _ehDirigido
        self.ehPonderado = _ehPonderado
        self.__rotulos = []
        self.__matriz_de_adjacencia = []
    

    def obterMatriz(self):
        return copy.deepcopy(self.__matriz_de_adjacencia)


    def qtdVertices(self):
        return len(self.__matriz_de_adjacencia)


    def qtdArestas(self):
        return sum([sum([1 for v in linha[i:] if v != self.sem_aresta]) for i, linha in enumerate(self.__matriz_de_adjacencia)])


    def grau(self, v):
        return len(self.vizinhos(v))


    def rotulo(self, v):
        return self.__rotulos[v - 1]


    def vizinhos(self, v):
        return [i + 1 for i, x in enumerate(self.__matriz_de_adjacencia[v - 1]) if x != self.sem_aresta]


    def haAresta(self, u, v):
        return self.__matriz_de_adjacencia[u - 1][v - 1] != self.sem_aresta


    def peso(self, u, v):
        return self.__matriz_de_adjacencia[u - 1][v - 1]


    def ler(self, arquivo):
        # Arquivo de entrada nao pode ter linha em branca(a mais)
        # a além disso, não pode ter espaços entre o rótulo ou seja, (Nova Trento não funciona) mas (Nova_Trento sim)
        with open(arquivo, "r") as arq:
            linhas = arq.read().split("\n")
        numero_de_vertices = int(linhas[0].split()[1])
        inicio_leitura_de_vertices = 1
        inicio_leitura_de_edges = numero_de_vertices + 2

        rotulos = linhas[inicio_leitura_de_vertices:inicio_leitura_de_edges - 1]
        self.__rotulos = [rotulo for v, rotulo in map(lambda x: x.split(), rotulos)]
        
        vertices = linhas[inicio_leitura_de_edges:]
        self.__matriz_de_adjacencia = [[self.sem_aresta] * numero_de_vertices for _ in range(numero_de_vertices)]
        for u, v, p in map(lambda x: map(float, x.split()), vertices):
            u = int(u) - 1
            v = int(v) - 1
            if not self.ehPonderado: p = 1
            self.__matriz_de_adjacencia[u][v] = p
            if not self.ehDirigido: self.__matriz_de_adjacencia[v][u] = p


    def obterArestas(self):
        vizinhos = []
        for l, linha in enumerate(self.__matriz_de_adjacencia):
            for c, elemento in enumerate(linha):
                if self.haAresta(l + 1, c + 1):
                    vizinhos.append((l + 1, c + 1))
        return vizinhos[:]
    

    def obterArestasParaVizinhos(self, v):
        return [(v, vizinho) for vizinho in self.vizinhos()]
    

    def obterArestasSemRepeticao(self):
        arestas = []
        for l, linha in enumerate(self.__matriz_de_adjacencia):
            for c, elemento in enumerate(linha):
                if self.haAresta(l + 1, c + 1) and (c + 1, l + 1) not in arestas:
                    arestas.append((l + 1, c + 1))
        return arestas[:]


    def __str__(self):
        return str(self.__matriz_de_adjacencia)
