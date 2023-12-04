

class HopcroftKarp:


    def emparelhar(self, G):
        D = [float('Inf') for v in range(0, G.qtdVertices() + 1)]
        mate = [0 for v in range(0, G.qtdVertices() + 1)]
        m = 0

        X, Y = G.obter_vertices_bipartido()
        
        while self.BFS(G, mate, D) == True:
            for x in X:
                if mate[x] == 0:
                    if self.DFS(G, mate, x, D) == True:
                        m += 1
        
        return m, mate[:]
    

    def BFS(self, G, mate, D):
        Q = []
        X, Y = G.obter_vertices_bipartido()

        for x in X:
            if mate[x] == 0:
                D[x] = 0
                Q.append(x)
            else:
                D[x] = float("Inf")

        D[0] = float("Inf")

        while len(Q) != 0:
            x = Q.pop(0)
            if D[x] < D[0]:
                for y in G.vizinhos(x):
                    if D[mate[y]] == float("Inf"):
                        D[mate[y]] = D[x] + 1
                        Q.append(mate[y])
        
        return D[0] != float("Inf")


    def DFS(self, G, mate, x, D):
        
        if x != 0:

            for y in G.vizinhos(x):
                if self.DFS(G, mate, mate[y], D) == True:
                    mate[y] = x
                    mate[x] = y
                    return True

            D[x] = float("Inf")
            return False
        
        return True