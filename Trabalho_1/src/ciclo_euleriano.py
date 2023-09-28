from grafo import Grafo

import random


class CicloEuleriano:
    
    def buscarSubcicloEuleriano(self, grafo: Grafo, v: int, arestas) -> list:
        ciclo = [v]
        t = v
        while True:
            
            arestasParaVizinhosV = grafo.obterArestasParaVizinhos(v)
            tem_aresta = False
            for aresta in arestas:
                if aresta in arestasParaVizinhosV:
                    tem_aresta = True
                    break

            if not tem_aresta:
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
            if v == t:
                break
        
        for x in ciclo:
            for w in grafo.vizinhos(x): #para cada x no ciclo e para cada W vizinho desse X tal que essa aresta eh falsa
                if not self.__c[x-1][w-1]:
                    r, subciclo = self.buscarSubcicloEuleriano(grafo, w)
                    if not r: #se r = false
                        return False, None
                    ciclo = ciclo[:ciclo.index(x)+1] + subciclo + ciclo[ciclo.index(x)+1:] #assumindo que ciclo...

        return True, ciclo
    
    def hierholzer(self, grafo):
        arestas = grafo.obterArestasSemRepeticao()
        v = random.randint(1, grafo.qtdVertices())

        print("Arestas:", arestas)
        print("Vertice inicial:", v)
        
        return None, True
        r, ciclo = self.buscarSubcicloEuleriano(grafo, v, arestas)
        if not r:
            return False, None
        
        # vai excluindo as arestas da lista, se sobrar quer dizer que tem aresta não visitada
        if len(arestas):
            return False, None
                
        return True, ciclo