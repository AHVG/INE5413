from grafo import Grafo
import argparse
from hopcroft_karp import HopcroftKarp


def main():
    """ Entrada do programa """

    # Paramêtro de programa
    # Recebe um caminho do arquivo em que está o grafo
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria o grafo a partir do arquivo passado por parâmetro
    grafo = Grafo(eh_dirigido=False, eh_ponderado=False)
    grafo.ler_bipartido(args.file)

    m, mate = HopcroftKarp().emparelhar(grafo)
    result = []
    for k in mate.keys():
        aresta = (k, mate[k])
        if (k, mate[k]) not in result and (mate[k], k) not in result:
            result.append(aresta)
    print("Emparelhamento máximo:", m)
    print("Arestas:", ", ".join([str(aresta) for aresta in result]))


if __name__ == "__main__":
    main()