from grafo import Grafo

import random


class CicloEuleriano:
    
    
    def buscarSubcicloEuleriano(self, grafo: Grafo, v: int, arestas: list) -> list:
        
        # define o vertice inicial
        t = v
        ciclo = [t]
        while True:
            # pega todas arestas que estão ligadas a v
            arestasVizinhasV = list(filter(lambda aresta: aresta[0] == v or aresta[1] == v, arestas))

            # Se não existir nenhuma aresta ligada a v, então não há caminho de volta para t
            # ou seja, não se tem um ciclo euleriano
            if not len(arestasVizinhasV):
                return None

            # escolhe arbitrariamente uma aresta de v e a remove das arestas
            arestaEsolhida = random.choice(arestasVizinhasV)
            arestas.remove(arestaEsolhida)
            
            # pega o próximo vertice do ciclo
            v = arestaEsolhida[0] if v == arestaEsolhida[1] else arestaEsolhida[1]
            ciclo.append(v)
            # Se o próximo vertice for o inicial, fechamos um ciclo euleriano
            if v == t:
                break

        # Aqui se faz a busca por subciclos
        novoCiclo = ciclo[:]
        for i, verticeCiclo in enumerate(ciclo):
            for origem, _ in arestas:
                # Se há alguma aresta não visistada ligada ao ciclo, então se faz a busca por um subciclo
                if origem == verticeCiclo:
                    subCiclo = self.buscarSubcicloEuleriano(grafo, origem, arestas)
                    if not subCiclo:
                        return None
                    # insere o subciclo no meio do ciclo
                    novoCiclo = novoCiclo[:i] + subCiclo + novoCiclo[i + 1:]

        return novoCiclo
    

    def hierholzer(self, grafo):
        # obtem todas arestas sem repeticao ((1,2) == (2,1)),
        # pois quando se visita a aresta (1,2) não é possível
        # voltar pela (2,1) (vide definição de um ciclo euleriano)
        arestas = grafo.obterArestasSemRepeticao()
        v = random.choice(arestas)[0]

        ciclo = self.buscarSubcicloEuleriano(grafo, v, arestas)
        if not ciclo:
            return None
        
        # vai excluindo as arestas da lista o algoritmo e se sobrar isso indica que tem aresta não visitada o que não deveria acontecer
        if len(arestas):
            return None
                
        return ciclo
