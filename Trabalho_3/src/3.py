from grafo import Grafo
import argparse
from coloracao import Coloracao

def main():
    """ Entrada do programa """

    # Paramêtro de programa
    # Recebe um caminho do arquivo em que está o grafo
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria o grafo a partir do arquivo passado por parâmetro
    grafo = Grafo(eh_ponderado=False)
    grafo.ler(args.file)

    resultado = Coloracao().lawler(grafo)
    cromaticos_por_vertice = Coloracao().definir_cromatico_por_vertice(grafo, resultado)
    print(f"Coloração mínima : {resultado}")
    for i,cor in enumerate(cromaticos_por_vertice): print(f"Vértice {i+1} -> cor {cor}")


if __name__ == "__main__":
    main()