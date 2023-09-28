from grafo import Grafo
from dijkstra import Dijkstra
import argparse

def main():
    # Paramêtro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    parser.add_argument('-v', '--vertice', action='store', type=int, required=True, help="Vertice que será analisado")
    args = parser.parse_args()

    # Cria um grafo direcionado e ponderado (pode ser não direcionado)
    grafo = Grafo(True, True)
    grafo.ler(args.file)
    inicio = args.vertice

    # Faz a busca e mostra na tela
    niveis = Dijkstra().busca(grafo, inicio)
    for no in niveis:
        lista_antecessores = Dijkstra().getAntecessores(no)
        lista_antecessores_com_virgula = ",".join(str(x) for x in lista_antecessores)
        print(f"{no.vertice}: {lista_antecessores_com_virgula}; d={int(no.distancia)}")


main()