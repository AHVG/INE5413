

class OrdenacaoTopologica:
    def __init__(self):
        self.tempo = 0
    
    def ordena(self, G):
        C = [False for _ in range(G.qtdVertices())]
        T = [float("Inf") for _ in range(G.qtdVertices())]
        F = [float("Inf") for _ in range(G.qtdVertices())]
        O = []
        for u in range(G.qtdVertices()):
            if not C[u]:
                self.DFS_visit_OT(G,u,C,T,F,O)
        return O

    def DFS_visit_OT(self,G,v,C,T,F,O):
        C[v] = True
        self.tempo += 1
        T[v] = self.tempo
        for (_,u) in G.obterArestasParaVizinhos(v):
            if not C[u-1]:
                self.DFS_visit_OT(G,u-1,C,T,F,O)
        self.tempo += 1
        F[v] = self.tempo
        O.insert(0,v) 