from collections import deque


def carregar_grafo(caminho_arquivo):
    """
    Lê um grafo de um arquivo texto e retorna:
      - matriz de adjacência (lista de listas)
      - número de vértices (n)

    Formato aceito (linhas):
      # comentários começam com #
      directed: true|false   (opcional, padrão: false)
      n: <numero_vertices>   (opcional)
      u v                    (uma aresta por linha, não ponderado)

    Vértices são numerados de 1 até n.
    A matriz terá tamanho (n+1) x (n+1), posição [0][*] é ignorada.
    """
    directed = False
    n = None
    arestas = []

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            # pula linha vazia ou comentário
            if not linha or linha.startswith("#"):
                continue

            # trata diretivas tipo "directed: false" ou "n: 5"
            if ":" in linha:
                chave, valor = [p.strip() for p in linha.split(":", 1)]
                chave = chave.lower()

                if chave == "directed":
                    valor_lower = valor.lower()
                    if valor_lower not in ("true", "false"):
                        raise ValueError(f"Valor inválido para 'directed': {valor}")
                    directed = (valor_lower == "true")
                    continue

                if chave == "n":
                    try:
                        n = int(valor)
                    except ValueError:
                        raise ValueError(f"Valor inválido para 'n': {valor}")
                    continue

                # Se tiver ":" mas não for chave conhecida, deixamos cair no erro abaixo
                # para não mascarar formato errado.

            # trata linha como aresta "u v"
            partes = linha.split()
            if len(partes) != 2:
                raise ValueError(f"Linha inválida no arquivo de grafo: '{linha}'")

            try:
                u = int(partes[0])
                v = int(partes[1])
            except ValueError:
                raise ValueError(f"Vértices devem ser inteiros: '{linha}'")

            arestas.append((u, v))

    if not arestas and n is None:
        raise ValueError("Arquivo não contém arestas nem valor de 'n'.")

    # Se n não foi informado, usamos o maior índice que apareceu
    if n is None:
        n = max(max(u, v) for (u, v) in arestas)

    # Cria matriz (n+1)x(n+1); ignoramos índice 0
    matriz = [[0] * (n + 1) for _ in range(n + 1)]

    # Preenche matriz com base nas arestas
    for (u, v) in arestas:
        if not (1 <= u <= n and 1 <= v <= n):
            raise ValueError(
                f"Aresta ({u}, {v}) contém vértice fora do intervalo 1..{n}"
            )

        matriz[u][v] = 1
        if not directed:
            matriz[v][u] = 1

    return matriz, n


def reconstruir_caminho(pais, origem, destino):
    """
    Reconstrói o caminho da origem até o destino usando o dicionário de pais.
    Retorna uma lista [origem, ..., destino] ou None se não houver caminho.
    """
    if destino not in pais:
        return None

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]

    caminho.reverse()
    return caminho


def bfs(matriz, origem, destino):
    """
    Busca em Largura (BFS) em um grafo representado por matriz de adjacência.

    Retorna:
      - lista com o caminho [origem, ..., destino], se existir
      - None, se não houver caminho

    Observações:
      - Considera vértices numerados de 1 até n.
      - matriz deve ser quadrada (n+1 x n+1), índice 0 ignorado.
    """
    n = len(matriz) - 1

    if not (1 <= origem <= n and 1 <= destino <= n):
        raise ValueError("origem/destino fora do intervalo válido.")

    fila = deque()
    fila.append(origem)

    visitados = set([origem])
    pais = {origem: None}

    while fila:
        atual = fila.popleft()

        if atual == destino:
            return reconstruir_caminho(pais, origem, destino)

        # percorre todos os possíveis vizinhos (1..n)
        for vizinho in range(1, n + 1):
            if matriz[atual][vizinho] == 1 and vizinho not in visitados:
                visitados.add(vizinho)
                pais[vizinho] = atual
                fila.append(vizinho)

    return None


def dfs(matriz, origem, destino):
    """
    Busca em Profundidade (DFS) recursiva em matriz de adjacência.

    Retorna:
      - lista com o caminho [origem, ..., destino], se existir
      - None, se não houver caminho
    """
    n = len(matriz) - 1

    if not (1 <= origem <= n and 1 <= destino <= n):
        raise ValueError("origem/destino fora do intervalo válido.")

    visitados = set()
    pais = {origem: None}

    def _dfs(atual):
        visitados.add(atual)

        if atual == destino:
            return True

        for vizinho in range(1, n + 1):
            if matriz[atual][vizinho] == 1 and vizinho not in visitados:
                pais[vizinho] = atual
                if _dfs(vizinho):
                    return True

        return False

    if _dfs(origem):
        return reconstruir_caminho(pais, origem, destino)

    return None
