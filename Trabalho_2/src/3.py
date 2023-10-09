from grafo import Grafo
from kruskal import Kruskal
import argparse

def main():
    # Paramêtro de programa
    # Recebe um caminho do arquivo em que está o grafo
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    # Cria o grafo a partir do arquivo passado por parâmetro
    grafo = Grafo()
    grafo.ler(args.file)

    # Obtendo a arvore mínima geradora com o algoritmo Kruskal
    a, peso = Kruskal().busca(grafo)

    # Formatando a saída e mostrando na tela
    resultado = ' '.join([f"{x}-{y}" for x, y in a])
    print(peso)
    print(resultado)
    

if __name__ == "__main__":
    main()