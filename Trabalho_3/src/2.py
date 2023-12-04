from grafo import Grafo
import argparse


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


if __name__ == "__main__":
    main()