from grafo import Grafo
from buscador_em_largura import BuscadorEmLargura

if __name__ == "__main__":
    grafo = Grafo()
    grafo.ler("./grafos/grafo_1.txt")
    print(BuscadorEmLargura().buscar(grafo, 1))
    print(BuscadorEmLargura().buscar(grafo, 2))
    print(BuscadorEmLargura().buscar(grafo, 3))

    grafo.ler("./grafos/grafo_2.txt")
    print(BuscadorEmLargura().buscar(grafo, 1))