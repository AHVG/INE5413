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
            for I in self.conjuntos_independentes_maximais([i+1 for i in range(G_linha.qtdVertices())], G_linha):
                s_i = list(S)
                for j in range(len(s_i)):
                    s_i[j] = S.index(s_i[j]) + 1                
                for I_ in I: s_i.remove(I_)
                i = f[str(s_i)]
                if X[i] + 1 < X[s]:
                    X[s] = X[i] + 1
        return X[-1]
            

    def conjuntos_independentes_maximais(self, vertices, grafo):
        S = self.conjunto_potencia(vertices)
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
        possibilidades = [list(range(1, coloracao_minima+1)) for i in range(grafo.qtdVertices())]
        solucao = [0 for _ in range(grafo.qtdVertices())]
        for possibilidade in possibilidades[0]:
            solucao[0] = possibilidade
            if self.pinta(grafo, possibilidades, solucao, 1): break
        return solucao

    def pinta(self, grafo, possibilidades, solucao, pintados):
        if pintados == grafo.qtdVertices(): return True
        for possibilidade in possibilidades[pintados]: 
            cor_permitida = True
            for vizinho in grafo.vizinhos(pintados+1):
                if solucao[vizinho-1] == possibilidade:
                    cor_permitida = False
                    break
            if cor_permitida:
                solucao[pintados] = possibilidade
                if self.pinta(grafo, possibilidades, solucao, pintados+1): return True
                solucao[pintados] = 0



    def conjunto_potencia(self, s):
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))