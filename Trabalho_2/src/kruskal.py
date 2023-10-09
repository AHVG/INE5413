from grafo import Grafo

# Numero de arestas da arvore geradora tem de ser numero de vertices -1
# Arestas nao podem formar ciclos
# Arestas tem de ser as de menor peso possivel
# Arestas tem de ligar todos os vertices
# Grafo tem de ser nao direcionado
# Da pra usar uma lista ligada para representar a arvore geradora

class Kruskal:
    
    def busca(self, grafo: Grafo):
        # Conjunto que armazena as arestas da arvore geradora
        a = set()

        # Estrutura para identificacao da arvore em cada vertice
        s = [{i} for i in range(1, grafo.qtdVertices() + 1)]
        
        arestas = grafo.obterArestasSemRepeticao()
        dic = dict()
        for i in arestas:
            # Dicionario com as arestas e seus respectivos pesos
            dic[i] = grafo.peso(i[0], i[1])
        
        # Ordenar o dicionario pela ordem crescente de peso
        ordered_dic = dict(sorted(dic.items(), key=lambda item: item[1]))

        # Atualizacao da identidade das arvores
        cont = 0
        peso = 0
        # Para cada par de arestas
        for u, v in ordered_dic.keys():
            # Se as arestas nao formarem ciclo
            if s[u - 1] != s[v - 1]:
                cont += 1
                # Adiciona a aresta na arvore geradora
                a.add((u,v))
                # Atualiza a identidade das arvores
                x = s[u-1].union(s[v-1])
                for y in x:
                    # Atualiza a identidade de cada vertice
                    s[y-1] = x
                # Atualiza o peso da arvore geradora
                peso += grafo.peso(u,v)
            # A arvore geradora tem de ter n-1 arestas
            # caso tiver, nao preciso mais iterar
            if cont == grafo.qtdVertices() - 1:
                break

        return a, peso