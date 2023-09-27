from grafo import Grafo
class CicloEuleriano:
    sem_aresta = float('inf')

    def __init__(self) -> None:
        self.__c = None
    
    def setar_matriz_c(self, matriz) -> None:
        self.__c = matriz
        for u in range(len(self.__c)):
            for v in range(len(self.__c)):
                if self.__c[u][v] != self.sem_aresta:
                    self.__c[u][v] = False
    
    def buscarSubcicloEuleriano(self, grafo: Grafo, v: int) -> list:
        ciclo = [v]
        t = v
        while v == t:
            break_ambos = False
            for u in grafo.vizinhos(v): # se nao existe nenhum vizinho de V tal que c[u][v] eh falso
                if self.__c[u-1][v-1]:
                    return False, None
            for i in range(len(self.__c)):
                for j in range(len(self.__c)):
                    if self.__c[i][j] == False: #selecionar e que pertence a E tal que Ce = False (por isso u = j+1 e v = i+1)
                        u = j+1
                        v= i+1
                        break_ambos = True
                        break
                if break_ambos:
                    break
    
            self.__c[v-1][u-1] = True #C[v][u] = True
            v = u
            ciclo.append(v)
        
        for x in ciclo:
            for w in grafo.vizinhos(x): #para cada x no ciclo e para cada W vizinho desse X tal que essa aresta eh falsa
                if not self.__c[x-1][w-1]:
                    r, subciclo = self.buscarSubcicloEuleriano(grafo, w)
                    if not r: #se r = false
                        return False, None
                    ciclo = ciclo[:ciclo.index(x)+1] + subciclo + ciclo[ciclo.index(x)+1:] #assumindo que ciclo...

        return True, ciclo
    
    def hierholzer(self, grafo, v):
        self.setar_matriz_c(grafo.getMatriz()) # para cada e pertencente a E Ce = false (cria uma nova matriz booleana) 
        #tem que fazer pra selecionar um  v arbitrario
        r, ciclo = self.buscarSubcicloEuleriano(grafo, v)
        if not r: #se r = false
            return False, None

        for i in range(len(self.__c)):
            for j in range(len(self.__c)):
                if self.__c[i][j] == False: #se ainda ha uma aresta nao visitada, entao retorna falso
                    return False, None
                
        return True, ciclo