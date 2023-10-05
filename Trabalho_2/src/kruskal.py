from grafo import Grafo

# Numero de arestas da arvore geradora tem de ser numero de vertices -1
# Arestas nao podem formar ciclos
# Arestas tem de ser as de menor peso possivel
# Arestas tem de ligar todos os vertices
# Grafo tem de ser nao direcionado


class Kruskal:
    
    def busca(self, grafo: Grafo):
        a = set()
        #estrutura para identificacao da arvore em cada vertice
        s = [{i} for i in range(1, grafo.qtdVertices() + 1)]

        arestas = grafo.obterArestas()
        dic = dict()
        for i in arestas:
            dic[i] = grafo.peso(i[0], i[1])
        
        #ordenar o dicionario pela ordem crescente de peso
        ordered_dic = dict(sorted(dic.items(), key=lambda item: item[1]))

        # Atualizacao da identidade das arvores
        for u,v in ordered_dic.keys():
            if s[u - 1] != s[v - 1]:
                a.add((u,v))
                x = s[u-1].union(s[v-1])
                for y in x:
                    s[y-1] = x
        return a