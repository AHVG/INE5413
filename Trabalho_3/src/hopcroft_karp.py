

class HopcroftKarp:


    def __init__(self):
        pass


    def emparelhar(self, G):
        D = [float('Inf') for v in G.qtdVertices()]
        mate = [None for v in G.qtdVertices()]
        m = 0
        while self.BFS(G, mate, D) == True:
            for x 