class No:
    # classe nó responsável por cada vértice do grafo
    # cada nó possui um vértice, um antecessor, uma distância e um booleano conhecido(se foi visitado ou não)
    def __init__(self, vertice) -> None:
        self.vertice = int(vertice)
        self.antecessor = None
        self.distancia = float('inf')
        self.conhecido = False
    
    # factory para criar as instâncias de nó
    @classmethod
    def create_node(cls, vertice):
        return cls(vertice)

class Dijkstra:
    # classe responsável por executar o algoritmo de Dijkstra
    def __init__(self) -> None:
        self.__vertices = []
    
    # método que retorna o vértice com menor distância
    def verticeMinimo(self):
        minVertice = None
        minDistance = -1

        for no in self.__vertices:
            # caso o nó não for conhecido, então ele é um candidato a ser o menor
            if no.conhecido == False:
                if minDistance == -1:
                    minVertice = no.vertice
                    minDistance = no.distancia
                else:
                    # se a distância do nó for menor que a distância mínima, então ele é o novo mínimo
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
