from grafo import Grafo
from ciclo_euleriano import CicloEuleriano
import argparse

def main():
    # Paramêtro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria um grafo não direcionado e ponderado (pode ser ponderado)
    grafo = Grafo(False, True)
    grafo.ler(args.file)

    # Busca o ciclo euleriano e mostra na tela o resultado
    ciclo = CicloEuleriano().hierholzer(grafo)
    if ciclo:
        print(1)
        print((", ".join([str(v) for v in ciclo])))
    else:
        print(0)

main()