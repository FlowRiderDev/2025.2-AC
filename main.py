from grafo import carregar_grafo, bfs, dfs


def main():
    # Nome fixo do arquivo de grafo na pasta do projeto
    caminho_arquivo = "grafo.txt"

    try:
        matriz, n = carregar_grafo(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao carregar o grafo de '{caminho_arquivo}': {e}")
        return

    print(f"Grafo carregado com sucesso a partir de '{caminho_arquivo}'.")
    print(f"Número de vértices: {n}")
    print("-" * 40)

    try:
        origem = int(input("Vértice de origem: "))
        destino = int(input("Vértice de destino: "))
    except ValueError:
        print("Origem e destino devem ser números inteiros.")
        return

    # BFS
    caminho_bfs = bfs(matriz, origem, destino)
    if caminho_bfs is not None:
        print(f"Caminho encontrado com BFS: {caminho_bfs}")
    else:
        print("Nenhum caminho encontrado com BFS.")

    # DFS
    caminho_dfs = dfs(matriz, origem, destino)
    if caminho_dfs is not None:
        print(f"Caminho encontrado com DFS: {caminho_dfs}")
    else:
        print("Nenhum caminho encontrado com DFS.")


if __name__ == "__main__":
    main()
