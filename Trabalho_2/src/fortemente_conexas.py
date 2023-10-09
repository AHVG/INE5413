import copy

class FortementeConexas:
    """
        Classe que obtem as componentes fortemente conexas de um grafo
    """

    def __init__(self):
        self.tempo = 0 # Passar por parâmetro não funciona, pois é uma copia


    def converter_para_componentes(self, A):
        """ 
        Função utilitária que dado um vetor de antecessores retorna um vetor de componentes
        
        Ex.:

        [None, None, 1] -> [[1, 2]]
        Obs.: Primeiro elemento não é considerado

        @param: vetor A de antecessores
        @return: vetor de componentes

        """

        # Converte o vetor A em uma lista com cada uma das componentes fortemente ligadas do grafo
        florestas = {}
        
        # Obtem todos os vertices que não possuem antecessor
        for i, v in enumerate(A[1:]):
            if v is None:
                florestas[i + 1] = [] # Perceba que é um dicionário e a chave é um inteiro
        
        # Para todo vertice, coloca-o em alguma das florestas de acordo com seu último antecessor não imediato (O que não tem antecessor)
        for v_analisado, v_anterior in enumerate(A[1:]):
            v_analisado += 1 # Mais 1, pois o enumerate gera de 0 a len(A[1:]) - 1 e os vertices são de 1 a len(A[1:])
            v_atual = v_analisado

            # Procura o antecessor que não tem antecessor e, quando encontra, insere na respectiva floresta o v_analisado
            # Basicamente vai pulando de antecessor a antecessor até que encontre aquele que não tem antecessor
            while True:

                if v_anterior is None:
                    florestas[v_atual].append(v_analisado)
                    break

                v_atual, v_anterior = v_anterior, A[v_atual]

        componentes = []

        # Formata as florestas para que sejam cada uma uma lista
        for ilha in florestas.keys():
            componentes.append(", ".join([str(i) for i in florestas[ilha]]))

        return copy.deepcopy(componentes)


    def buscar_por_componentes(self, grafo):
        """
        Função que busca por componentes conexas
        
        @param: grafo que será analisado
        @return: componentes conexas do grafo

        """

        # Primeira DFS
        C, T, A, F = self.DFS(grafo)

        # Cria o grafo "transposto"
        grafo_transposto = grafo.obterTransposto() # O bom seria uma fabrica para criar grafos

        # Segunda DFS, só que adapatada para pegar os vertices com maior tempo final primeiro
        C_transposto, T_transposto, A_transposto, F_transposto = self.DFS_adaptado(grafo_transposto, F)

        # Convertendo o vetor de antecessores para uma lista de componentes
        return self.converter_para_componentes(A_transposto)


    def DFS(self, grafo):
        """
        Busca por profundidade

        @param: grafo em que será aplicado a busca por profundidade
        @return: C, T, F, A onde C é o vetor de visistados, T o de tempo inicial, F o de final e A de antecessor

        """

        # Criando os vetores do retorno com um indice a mais para facilitar a implementação do algoritmo
        # Todas listas tem um elmento inutil, o primeiro, para não ficar colocando - 1 ou + 1 nos indices
        C = [False          for _ in range(grafo.qtdVertices() + 1)] # Todos os vertices não visitados
        T = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)] # Tempo inicial infinito
        F = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)] # Tempo final infinito
        A = [None           for _ in range(grafo.qtdVertices() + 1)] # Todos vertices sem antecessores

        # Zerando o contador de tempo
        self.tempo = 0

        # Fazendo as visitadas
        for v in range(1, grafo.qtdVertices() + 1):
            if not C[v]:
                self.DFS_visit(grafo, v, C, T, A, F)

        return C, T, A, F


    def DFS_adaptado(self, grafo, F_linha):
        """
        Busca por profundidade adapatada para que se escolha primeiro os vertices com maior valor de F

        @param: grafo em que será aplicado a busca por profundidade
        @return: C, T, F, A onde C é o vetor de visistados, T o de tempo inicial, F o de final e A de antecessor
        
        """

        # Criando os vetores do retorno com um indice a mais para facilitar a implementação do algoritmo
        # Todas listas tem um elmento inutil, o primeiro, para não ficar colocando - 1 ou + 1 nos indices
        C = [False          for _ in range(grafo.qtdVertices() + 1)] # Todos os vertices não visitados
        T = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)] # Tempo inicial infinito
        F = [float("Inf")   for _ in range(grafo.qtdVertices() + 1)] # Tempo final infinito
        A = [None           for _ in range(grafo.qtdVertices() + 1)] # Todos vertices sem antecessores

        # Zerando o contador de tempo e ordenando a lista de vertices de acordo com seu tempo final (os com maior valor vem primeiro)
        self.tempo = 0
        vertices_ordenados = sorted(zip(list(range(1, grafo.qtdVertices() + 1)), F_linha[1:]),
                                     key=lambda x: x[1], reverse=True)

        # Fazendo as visitas
        for v, _ in vertices_ordenados:
            if not C[v]:
                self.DFS_visit(grafo, v, C, T, A, F)

        return C, T, A, F


    def DFS_visit(self, grafo, v, C, T, A, F):
        """
        Função que visita efetivamente um vertice

        @param: grafo em que foi aplicado a busca por pronfundidade
        @param: v vertice atual
        @param: C vetor de visitados
        @param: T vetor do tempo inicial
        @param: A vetor de antecessores
        @param: F vetor de tempo final

        @return: Nada
        """
        # Define o vertice atual como visitado e seu tempo inicial
        C[v] = True
        self.tempo += 1
        T[v] = self.tempo

        # Visita todos seus vizinhos ainda não visitados
        for u in grafo.vizinhos(v):
            if not C[u]:
                A[u] = v
                self.DFS_visit(grafo, u, C, T, A, F)

        # Define seu tempo final
        self.tempo += 1
        F[v] = self.tempo
