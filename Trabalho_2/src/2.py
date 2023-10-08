from grafo import Grafo
import argparse
from ordenacao_topologica import OrdenacaoTopologica

def main():
    # Paramêtro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    grafo = Grafo(eh_ponderado=False, eh_dirigido=True)
    grafo.ler(args.file)

    ordenacao = OrdenacaoTopologica().ordena(grafo)
    ordenacao_rotulada = [grafo.rotulo(v) for v in ordenacao]
    print(" -> ".join(ordenacao_rotulada))

        
if __name__ == "__main__":
    main()