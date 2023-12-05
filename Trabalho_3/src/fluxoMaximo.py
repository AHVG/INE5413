from grafo import Grafo

class EdmondsKarp:
    def busca(self, grafo: Grafo, s: int, t: int, grafo_residual: Grafo):
        # lista de visitados e lista de antecessores
        visitados = [False] * grafo.qtdVertices()
        antecessores = [None] * grafo.qtdVertices()

        visitados[s - 1] = True
        fila = [s]
        while fila:
            u = fila.pop(0)
            for v in grafo.vizinhos(u):
                if not visitados[v - 1] and grafo_residual.peso(u, v) > 0:
                    visitados[v - 1] = True
                    antecessores[v - 1] = u
                    if v == t:
                        p = [t]
                        w = t
                        while w != s:
                            w = antecessores[w - 1]
                            p.insert(0, w)
                        return p
                    fila.append(v)
        return None

