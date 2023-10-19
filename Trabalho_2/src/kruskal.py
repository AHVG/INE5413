from grafo import Grafo

# Numero de arestas da arvore geradora tem de ser numero de vertices -1
# Arestas nao podem formar ciclos
# Arestas tem de ser as de menor peso possivel
# Arestas tem de ligar todos os vertices
# Grafo tem de ser nao direcionado
# Da pra usar uma lista ligada para representar a arvore geradora

class Kruskal:
    """
    Classe que obtêm a arvore mínima geradora
    """
    
    def busca(self, G: Grafo) -> (set, float):
        """
        Função que busca pela arvore mínima geradora do grafo G

        @param: G grafo que será analisado

        @return: Os vertices da arvore mínima geradora
        """
        # Estrutura para identificacao da arvore em cada vertice
        A = set()
        S = [{i} for i in range(1, G.qtdVertices() + 1)]

        # Criando um dicionario que mapeia aresta para peso ordenado de acordo com o peso
        arestas = G.obterArestasSemRepeticao()
        arestas_para_peso = dict()

        for i in arestas:
            arestas_para_peso[i] = G.peso(i[0], i[1])
        
        arestas_para_peso_ordenada = dict(sorted(arestas_para_peso.items(), key=lambda item: item[1]))

        # Define um valor inicial a variável que indica parada (numero_de_arestas_adicionadas) e
        # o peso da arvora mínima
        numero_de_arestas_adicionadas = 0
        peso = 0

        # Cria interativamente a arvore mínima geradora
        for u, v in arestas_para_peso_ordenada.keys():

            # Se não tiver um ciclo, então adiciona a aresta a arvore e atualiza as arvores de S
            if S[u - 1] != S[v - 1]:
                numero_de_arestas_adicionadas += 1 # 
                A.add((u,v))
                x = S[u-1].union(S[v-1])

                for y in x:
                    S[y-1] = x

                peso += G.peso(u,v)

            # Se adicionou número de vertices - 1 arestas, então termina o algoritmo
            if numero_de_arestas_adicionadas == G.qtdVertices() - 1:
                break

        return A, peso