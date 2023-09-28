from grafo import Grafo
from floyd_warshall import FloydWarshall
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    grafo = Grafo(True, True)
    grafo.ler(args.file)
    distanciasMinimas = FloydWarshall().calcular(grafo)
    for linha in distanciasMinimas:
        print(" ".join([str(e) for e in linha]))


main()