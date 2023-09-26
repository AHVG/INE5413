from grafo import Grafo
from dijkstra import Dijkstra
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    parser.add_argument('-v', '--vertice', action='store', type=int, required=True, help="Vertice que será analisado")
    args = parser.parse_args()

    grafo = Grafo(True, True)
    grafo.ler(args.file)
    inicio = args.vertice
    niveis = Dijkstra().busca(grafo, inicio)


main()