# 2025.2-AC // Projeto de Grafos – Leitura, BFS e DFS

Este projeto implementa:

- Leitura de um grafo a partir de um arquivo texto.
- Representação do grafo como **matriz de adjacência**.
- Busca em Largura (**BFS**) para encontrar um caminho entre dois vértices.
- Busca em Profundidade (**DFS**) para encontrar um caminho entre dois vértices.

A ideia é ser simples, direto e fácil de integrar com uma interface futura.

---

## Formato do Arquivo de Entrada (`.txt`)

O grafo é definido em um arquivo texto com as seguintes regras:

1. **Comentários**:
   - Linhas que começam com `#` são ignoradas.
   - Podem ser usadas para descrição ou exemplos.

2. **Direcionalidade (opcional)**:
   - Linha opcional:
     ```text
     directed: true
     ```
     ou
     ```text
     directed: false
     ```
   - Padrão (se não informado): `false` (grafo não-direcionado).
   - Se `directed: true`, cada linha `u v` representa uma aresta **apenas de `u` para `v`**.
   - Se `directed: false`, cada linha `u v` adiciona aresta em ambos os lados: `u-v` e `v-u`.

3. **Número de vértices (opcional)**:
   - Linha opcional:
     ```text
     n: 5
     ```
   - Se não for informado, `n` será definido automaticamente como o maior índice de vértice presente nas arestas.

4. **Arestas (obrigatório)**:
   - Após as linhas opcionais, cada linha com dois inteiros representa uma aresta:
     ```text
     u v
     ```
   - Exemplo:
     ```text
     1 2
     1 3
     2 4
     3 5
     ```

5. **Intervalo de vértices**:
   - Os vértices devem ser numerados de `1` até `n`.
   - Qualquer vértice fora desse intervalo é considerado erro de entrada.

---

## Exemplo de Arquivo Válido

Exemplo de grafo não-direcionado com 5 vértices:

```text
# Grafo simples de exemplo
directed: false
n: 5

1 2
1 3
2 4
3 5
