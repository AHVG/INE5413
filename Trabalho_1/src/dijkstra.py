class No:
    
    def __init__(self, vertice) -> None:
        self.vertice = int(vertice)
        self.antecessor = None
        self.distancia = float('inf')
        self.conhecido = False
    

    @classmethod
    def create_node(cls, vertice):
        return cls(vertice)

class Dijkstra:


    def __init__(self) -> None:
        self.__vertices = []
    

    # método que retorna o vértice com menor distância
    def verticeMinimo(self):
        minVertice = None
        minDistance = -1

        for no in self.__vertices:
            if no.conhecido == False:
                if minDistance == -1:
                    minVertice = no.vertice
                    minDistance = no.distancia
                else:
                    if minDistance > no.distancia:
                        minVertice = no.vertice
                        minDistance = no.distancia
        return minVertice
    

    # método que fará a execução do Dijkstra
    def busca(self, grafo, origem):
        # cria nós para cada vértice do grafo
        for i in range(1, grafo.qtdVertices()+1):
            self.__vertices.append(No.create_node(i))
        
        # origem recebe distância 0
        self.__vertices[origem - 1].distancia = 0

        while True:
            # pega o vértice com menor distância
            minVertice = self.verticeMinimo()

            # se for None, significa que todos ja foram visitados
            if minVertice is None:
                break

            # seto o vértice como conhecido
            self.__vertices[minVertice-1].conhecido = True

            # pego seus vizinhos
            vizinhos = grafo.vizinhos(minVertice)

            #itero por cada vizinho
            for v in vizinhos:
                if self.__vertices[v-1].conhecido == False:
                    # If Dv > Du + w((u,v))
                    if self.__vertices[v-1].distancia > self.__vertices[minVertice-1].distancia + grafo.peso(minVertice, v):
                        self.__vertices[v-1].distancia = self.__vertices[minVertice-1].distancia + grafo.peso(minVertice, v)
                        self.__vertices[v-1].antecessor = self.__vertices[minVertice-1]

        return self.__vertices


    # método que vai retornar a lista de antecessores de cada vértice, ou seja
    # seu caminho até o vértice de origem
    def getAntecessores(self, no):
        lista_antecessores = []
        while True:
            lista_antecessores.append(no.vertice)
            if no.antecessor == None:
                break
            else:
                no = no.antecessor

        return lista_antecessores[::-1]
