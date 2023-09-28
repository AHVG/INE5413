from grafo import Grafo
from ciclo_euleriano import CicloEuleriano
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    grafo = Grafo(False, True)
    grafo.ler(args.file)
    tem, ciclo = CicloEuleriano().hierholzer(grafo)



main()