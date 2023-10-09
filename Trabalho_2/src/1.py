from grafo import Grafo
from fortemente_conexas import FortementeConexas
import argparse


def main():
    # Paramêtro de programa
    # Recebe um caminho do arquivo em que está o grafo
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria o grafo a partir do arquivo passado por parâmetro
    grafo = Grafo(eh_dirigido=True, eh_ponderado=False)
    grafo.ler(args.file)

    # Obtendo as componentes fortemente conexas
    componentes = FortementeConexas().buscar_por_componentes(grafo)
    
    # Mostrando no terminal cada uma
    for componente in componentes:
        print(componente)


if __name__ == "__main__":
    main()