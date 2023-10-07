

class FortementeConexas:


    def __init__(self):
        pass


    def buscarPorComponentes(self, grafo):
        C, T, A_linha, F = self.DFS(grafo)

        grafo_transposto = grafo.obterTransposto() # O bom seria uma fabrica para criar grafos
        
        C_transposto, T_transposto, A_linha_transposto, F_transposto = self.DFSAdaptado(grafo_transposto, F)

        return A_linha_transposto

    # TODO: Colocar numa classe esse DFS's
    def DFS(self, grafo):
        pass


    def DFSAdaptado(self, grafo, F):
        pass


    def DFSVisit(self, grafo, v, vistados, temposIniciais, anteriores, temposFinais):
        pass
