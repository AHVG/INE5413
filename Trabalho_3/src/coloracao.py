from itertools import chain, combinations
from grafo import Grafo
class Coloracao:

    def lawler(self, grafo):
        X = [float("inf") for _ in range(pow(2, grafo.qtdVertices()))]
        X[0] = 0
        S_ = self.conjunto_potencia([i+1 for i in range(grafo.qtdVertices())])
        f = {'[]': 0}
        for s in range(1, len(S_)):
            S = S_[s]
            f[str(list(S))] = s
            matriz_adjacencia = [[float("Inf")] * len(S) for _ in S]
            for u in range(len(S)):
                for v in range(u+1, len(S)):
                    if grafo.haAresta(S[u], S[v]): 
                        matriz_adjacencia[u][v] = 1
                        matriz_adjacencia[v][u] = 1

            G_linha = Grafo(eh_dirigido=False, eh_ponderado=False, matriz=matriz_adjacencia)
            for I in self.conjuntos_independentes_maximais(G_linha):
                s_i = list(S)[:]
                for j in range(len(s_i)):
                    s_i[j] = S.index(s_i[j]) + 1                
                for I_ in I: s_i.remove(I_)
                i = f[str(s_i)]
                if X[i] + 1 < X[s]:
                    X[s] = X[i] + 1
        return X[-1]
            

    def conjuntos_independentes_maximais(self, grafo):
        S = self.conjunto_potencia([i+1 for i in range(grafo.qtdVertices())])
        S.reverse()
        R = []
        for x in S:
            c = True
            for v in x:
                for u in x:
                    if grafo.haAresta(u,v):
                        c = False
                        break
            if c:
                subconjuntos_x = self.conjunto_potencia(x)
                for subconjunto in subconjuntos_x:
                    if subconjunto in S: S.remove(subconjunto)
                R.append(x)
        return R
    
    def definir_cromatico_por_vertice(self, grafo, coloracao_minima):
        cores_por_vertice = [0 for _ in range(grafo.qtdVertices())]
        conjuntos_independentes_maximais = self.conjuntos_independentes_maximais(grafo)
        coloridos = []
        for conjunto in conjuntos_independentes_maximais:
            todos_coloridos = True
            for elemento in conjunto:
                if elemento not in coloridos:
                    todos_coloridos = False 
                    break
            if not todos_coloridos:
                for elemento in conjunto:
                    if not cores_por_vertice[elemento - 1]: 
                        cores_por_vertice[elemento - 1] = coloracao_minima
                        coloridos.append(elemento)
                coloracao_minima -= 1
        return cores_por_vertice


    def conjunto_potencia(self, s):
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))