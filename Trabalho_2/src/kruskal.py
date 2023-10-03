from grafo import Grafo

class Kruskal:

    def uniao(self, A,  B):
        x = []
        for a in A:
            x.append(a)
        for b in B:
            x.append(b)
        return x
    
    def busca(self, grafo: Grafo):
        a = set()
        s = [{i} for i in range(1, grafo.qtdVertices() + 1)]

        arestas = grafo.obterArestas()
        dic = dict()
        for i in arestas:
            dic[i] = grafo.peso(i[0], i[1])
        
        #ordenar o dicionario pela ordem crescente de peso
        ordered_dic = dict(sorted(dic.items(), key=lambda item: item[1]))

        for u,v in ordered_dic.keys():
            if s[u - 1] != s[v - 1]:
                a.add((u,v))
                x = self.uniao(s[u - 1], s[v - 1])
                for y in x:
                    s[y - 1] = x
        return a