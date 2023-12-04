from grafo import Grafo
import argparse
from fluxoMaximo import EdmondsKarp

def main():
    """ Entrada do programa """

    # Paramêtro de programa
    # Recebe um caminho do arquivo em que está o grafo
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria o grafo a partir do arquivo passado por parâmetro
    grafo = Grafo(eh_ponderado=False)
    grafo.ler(args.file)
    grafo_residual = grafo.obterGrafoResidual()
    fluxo = 0
    while True:
        resultado = EdmondsKarp().busca(grafo, 1, grafo.qtdVertices(), grafo_residual)
        if resultado is None:
            break
        for u in range(len(resultado)-1):
            vertice_u = resultado[u]
            vertice_v = resultado[u + 1]
            minimo = grafo.sem_aresta
            if grafo_residual.peso(vertice_u, vertice_v) < minimo:
                minimo = grafo_residual.peso(vertice_u, vertice_v)
                
        fluxo += minimo
        for u in range(len(resultado)-1):
            vertice_u = resultado[u]
            vertice_v = resultado[u + 1]
            grafo_residual.atualizaPesoAresta(vertice_u, vertice_v, grafo_residual.peso(vertice_u, vertice_v) - minimo)
            grafo_residual.atualizaPesoAresta(vertice_v, vertice_u, grafo_residual.peso(vertice_v, vertice_u) + minimo)
    
    print("Fluxo maximo: ", fluxo)
        



if __name__ == "__main__":
    main()