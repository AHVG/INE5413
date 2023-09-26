from grafo import Grafo
from ciclo_euleriano import CicloEuleriano
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    parser.add_argument('-v', '--vertice', action='store', type=int, required=True, help="Vertice que será analisado")
    args = parser.parse_args()

    grafo = Grafo(True, True)
    grafo.ler(args.file)
    inicio = args.vertice
    niveis = CicloEuleriano().EulerianTour(grafo, inicio)
    cont = 0
    if(niveis != None):
        print("1")
        for i in niveis:
            print(i, end=" ") #tem que arrumar o print dps
        print()
    else:
        print("Não é euleriano")

main()