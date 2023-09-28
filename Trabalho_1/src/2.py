import argparse

from grafo import Grafo
from buscador_em_largura import BuscadorEmLargura


def main():
    # Parametro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    parser.add_argument('-v', '--vertice', action='store', type=int, required=True, help="Vertice que será analisado")
    args = parser.parse_args()

    # Cria um grafo não direcionado e não ponderado (pode ser ponderado) de acordo com o arquivo de entrada
    grafo = Grafo(False, False)
    grafo.ler(args.file)

    # Faz a busca em largura e retorna os níveis
    niveis = BuscadorEmLargura().buscar(grafo, args.vertice)
    for i, nivel in enumerate(niveis):
        print(f"{i}: " + ",".join([str(v) for v in nivel]))
        

main()