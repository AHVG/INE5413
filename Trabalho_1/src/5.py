from grafo import Grafo
from floyd_warshall import FloydWarshall
import argparse

def main():
    # Paramêtro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria um grafo direcionado e ponderado (pode ser não direcionado)
    grafo = Grafo(True, True)
    grafo.ler(args.file)

    # Calcula os caminhos minimos e mostra na tela a matriz
    distanciasMinimas = FloydWarshall().calcular(grafo)
    for linha in distanciasMinimas:
        print(" ".join([str(e) for e in linha]))


main()