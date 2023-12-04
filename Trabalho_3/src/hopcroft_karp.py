

class HopcroftKarp:


    def emparelhar(self, G):
        D = dict(zip([v for v in range(1, G.qtdVertices() + 1)],
                     [float("Inf") for v in range(1, G.qtdVertices())]))
        mate = dict(zip([v for v in range(1, G.qtdVertices() + 1)],
                        [None for v in range(1, G.qtdVertices() + 1)]))
        m = 0

        X, Y = G.obter_vertices_bipartido()
        
        while self.BFS(G, mate, D) == True:
            for x in X:
                if mate[x] == None:
                    if self.DFS(G, mate, x, D) == True:
                        m += 1
    
        return m, mate.copy()
    

    def BFS(self, G, mate, D):
        Q = []
        X, Y = G.obter_vertices_bipartido()

        for x in X:
            if mate[x] == None:
                D[x] = 0
                Q.append(x)
            else:
                D[x] = float("Inf")

        D[None] = float("Inf")

        while len(Q) != 0:
            x = Q.pop(0)
            if D[x] < D[None]:
                for y in G.vizinhos(x):
                    if D[mate[y]] == float("Inf"):
                        D[mate[y]] = D[x] + 1
                        Q.append(mate[y])
        
        return D[None] != float("Inf")


    def DFS(self, G, mate, x, D):
        
        if x != None:

            for y in G.vizinhos(x):
                if D[mate[y]] == D[x] + 1:
                    if self.DFS(G, mate, mate[y], D) == True:
                        mate[y] = x
                        mate[x] = y
                        return True

            D[x] = float("Inf")
            return False
        
        return True