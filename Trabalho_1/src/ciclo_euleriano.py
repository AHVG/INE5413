from grafo import Grafo
class CicloEuleriano:
    def __init__(self) -> None:
        self.__c = None
    
    def setar_matriz_c(self, matriz) -> None:
        self.__c = matriz
        for u in range(len(self.__c)):
            for v in range(len(self.__c)):
                if self.__c[u][v] != self.sem_aresta:
                    self.__c[u][v] = False
                else:
                    self.__c[u][v] = True
    
    def buscarSubcicloEuleriano(self, grafo: Grafo, v: int) -> list:
        ciclo = [v]
        t = v
        while v == t:
            tinha_nao_visitada = False
            for u in grafo.vizinhos(v):
                if grafo.haAresta(u,v) and self.__c[u-1][v-1] == False:
                    self.__c[u-1][v-1] = True
                    v = u
                    ciclo.append(v)
                    tinha_nao_visitada = True
            if not tinha_nao_visitada:
                return False, None
        
        for x in ciclo:
            for w in grafo.vizinhos(x):
                if grafo.haAresta(x,w):
                    visitada = self.__c[x-1][w-1]
                if not visitada:
                    tem_subciclo, subciclo = self.buscarSubcicloEuleriano(grafo, w)
                    if not tem_subciclo:
                        return False, None
                    ciclo = ciclo[:ciclo.index(x)+1] + subciclo + ciclo[ciclo.index(x)+1:]

        return True, ciclo
    
    def hierholzer(self, grafo):
        print(grafo)
        copia_matriz = grafo.getMatriz()
        self.setar_matriz_c(copia_matriz)
        print(grafo)
        v = 2
        r, ciclo = self.buscarSubcicloEuleriano(grafo, v)
        if not r:
            return False, None

        for i in range(len(self.__c)):
            for j in range(len(self.__c)):
                if self.__c[i][j] == False:
                    return False, None
                
        return True, ciclo
        
                    