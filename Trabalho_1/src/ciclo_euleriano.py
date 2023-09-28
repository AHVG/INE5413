from grafo import Grafo

import random


class CicloEuleriano:
    
    def buscarSubcicloEuleriano(self, grafo: Grafo, v: int, arestas: list) -> list:
        ciclo = [v]
        t = v
        while True:

            arestasVizinhasV = list(filter(lambda aresta: aresta[0] == v, arestas))
            if not len(arestasVizinhasV):
                return False, None

            arestaEsolhida = random.choice(arestasVizinhasV)
            arestas.remove(arestaEsolhida)
            v = arestaEsolhida[1]
            ciclo.append(v)
            if v == t:
                break

        novoCiclo = ciclo[:]
        for i, verticeCiclo in enumerate(ciclo):
            for origem, destino in arestas:
                if origem == verticeCiclo:
                    r, subCiclo = self.buscarSubcicloEuleriano(grafo, origem, arestas)
                    if not r:
                        return False, None
                    novoCiclo = novoCiclo[:i] + subCiclo + novoCiclo[i + 1:]

        return True, novoCiclo
    
    def hierholzer(self, grafo):
        arestas = grafo.obterArestasSemRepeticao()
        v = random.randint(1, grafo.qtdVertices())

        print("Arestas:", arestas)
        print("Vertice inicial:", v)
        
        r, ciclo = self.buscarSubcicloEuleriano(grafo, v, arestas)
        if not r:
            return False, None
        
        # vai excluindo as arestas da lista, se sobrar quer dizer que tem aresta não visitada
        if len(arestas):
            return False, None
                
        return True, ciclo