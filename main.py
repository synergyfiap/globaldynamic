from typing import List, Tuple, Dict

Project = Tuple[str, int, int]  # (nome, valor, horas)

# ---------------------------------------------------------
# Implementações do problema 0/1 Knapsack (Mochila 0/1)
# Cada versão tem comentários explicativos sobre a lógica,
# complexidade e os casos base utilizados.
# ---------------------------------------------------------

# ------------------ FASE 1: Estratégia Gulosa ------------------

def greedy_knapsack(projects: List[Project], capacity: int) -> Tuple[List[Project], int]:
    """
    Abordagem gulosa: ordena os projetos pela razão valor/horas (valor por unidade de hora)
    e seleciona enquanto houver capacidade disponível.

    Observação importante: esta estratégia NÃO garante solução ótima para o problema 0/1
    (cada item só pode ser aceito ou recusado inteiramente). A ordenação por razão é útil
    como heurística (rápida), mas pode falhar (caso 2 nos testes demonstra isso).

    Retorna a lista de projetos escolhidos e o valor total obtido.
    """

    # Ordena por razão (valor/horas). Em caso de empate, prioriza maior valor absoluto.
    # sorted_projects[0] será o projeto com maior valor por hora.
    sorted_projects = sorted(projects, key=lambda p: (p[1] / p[2], p[1]), reverse=True)

    chosen, total_value = [], 0
    remaining = capacity  # horas restantes de capacidade

    # Seleção simples: pega cada projeto se couber nas horas restantes
    for proj in sorted_projects:
        name, value, hours = proj
        # Se o projeto cabe na capacidade restante, selecionamos ele.
        if hours <= remaining:
            chosen.append(proj)
            total_value += value
            remaining -= hours

    return chosen, total_value


# ------------------ FASE 2: Solução Recursiva Pura ------------------

def recursive_knapsack(projects: List[Project], capacity: int) -> int:
    """
    Implementação recursiva direta que explora todas as possibilidades.

    Definição recursiva (padrão para 0/1 knapsack):
      - helper(i, c) = valor ótimo considerando apenas os i primeiros projetos
        com capacidade c.
      - Caso base: i == 0 (sem projetos) ou c == 0 (capacidade zero) -> 0.
      - Recorrência: para o i-ésimo projeto (índice i-1 na lista):
          * se hours > c -> não cabe -> igual a helper(i-1, c)
          * senão -> max(nao pegar, pegar) = max(helper(i-1, c), value + helper(i-1, c-hours))

    Esta versão é didática, mas sua complexidade de tempo é O(2^n) no pior caso,
    porque explora todas as combinações possíveis.
    """

    n = len(projects)

    def helper(i, c):
        # Caso base da recursão: sem itens (i == 0) ou sem capacidade (c == 0)
        # não há valor a ser obtido.
        if i == 0 or c == 0:
            return 0

        name, value, hours = projects[i - 1]  # projeto atual a ser considerado

        # Se o projeto não cabe na capacidade atual, não podemos escolhê-lo.
        if hours > c:
            return helper(i - 1, c)

        # Caso contrário, decidimos entre não pegar ou pegar o projeto.
        # "não pegar" = helper(i-1, c)
        # "pegar"    = value + helper(i-1, c - hours)
        return max(helper(i - 1, c), value + helper(i - 1, c - hours))

    return helper(n, capacity)


# ------------------ FASE 3: Top-Down com Memoizacao ------------------

def memoized_knapsack(projects: List[Project], capacity: int) -> int:
    """
    Versão top-down (recursiva) com memoização para evitar recomputações.

    A ideia: armazenar os resultados de subproblemas (i, c) em um dicionário "memo",
    de modo que cada estado é calculado no máximo uma vez. Isso reduz o tempo para
    O(n * capacity) e usa espaço O(n * capacity) para a tabela de memoização.
    """

    memo = {}  # chave: (i, c) -> valor ótimo para os i primeiros projetos e capacidade c
    n = len(projects)

    def helper(i, c):
        # Caso base: sem itens ou sem capacidade
        if i == 0 or c == 0:
            return 0

        # Se já calculamos o estado (i, c), retornamos imediatamente
        if (i, c) in memo:
            return memo[(i, c)]

        name, value, hours = projects[i - 1]

        if hours > c:
            # Projeto não cabe: herdamos a solução sem ele
            memo[(i, c)] = helper(i - 1, c)
        else:
            # Testamos as duas opções e guardamos o melhor resultado
            memo[(i, c)] = max(helper(i - 1, c), value + helper(i - 1, c - hours))

        return memo[(i, c)]

    return helper(n, capacity)


# ------------------ FASE 4: Bottom-Up ------------------

def bottom_up_knapsack(projects: List[Project], capacity: int) -> int:
    """
    Implementação iterativa de programação dinâmica (bottom-up).

    Construímos uma tabela T de dimensão (n+1) x (capacity+1), onde
      T[i][c] representa o valor máximo que pode ser obtido usando os
      primeiros i projetos (índices 0..i-1) com capacidade c.

    - Linha i = 0: sem projetos -> valor 0 para qualquer capacidade.
    - Coluna c = 0: capacidade zero -> valor 0 para qualquer número de projetos.

    A transição é análoga à recursão:
      - se hours > c: T[i][c] = T[i-1][c]  (não cabe)
      - senão:       T[i][c] = max(T[i-1][c], value + T[i-1][c-hours])

    A resposta ótima será T[n][capacity].
    """

    n = len(projects)
    # Inicializa a tabela com zeros. T tem (n+1) linhas (0..n) e (capacity+1) colunas (0..capacity).
    T = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, value, hours = projects[i - 1]
        for c in range(capacity + 1):
            # Interpretação de T[i][c]: valor ótimo usando os i primeiros itens com capacidade c
            if hours > c:
                # O i-ésimo item (projects[i-1]) não cabe: copiamos o melhor sem ele
                T[i][c] = T[i - 1][c]
            else:
                # Testamos não pegar (T[i-1][c]) ou pegar (value + T[i-1][c-hours])
                T[i][c] = max(T[i - 1][c], value + T[i - 1][c - hours])

    # T[n][capacity] contém o valor ótimo considerando todos os n projetos.
    return T[n][capacity]


# ------------------ EXECUÇÃO E TESTES ------------------
if __name__ == "__main__":

    casos = [
        # Caso 1: exemplo simples onde existe combinação ótima conhecida
        ([("A", 12, 4), ("B", 10, 3), ("C", 7, 2), ("D", 4, 3)], 10, 29),

        # Caso 2 — demonstra que a gulosa pode falhar: melhor é Y+Z = 220
        ([("X", 60, 10), ("Y", 100, 20), ("Z", 120, 30)], 50, 220),

        # Caso 3 — capacidade zero
        ([("P1", 10, 5), ("P2", 20, 3)], 0, 0),

        # Caso 4 — nenhum item cabe (todos exigem mais horas que a capacidade)
        ([("I1", 5, 10), ("I2", 7, 11)], 5, 0),

    ]

    print("===== TESTES COMPLETOS =====\n")
    for idx, (projs, cap, esperado) in enumerate(casos, 1):
        print(f"\n--- Caso {idx} ---")
        print("Projetos:", projs)
        print("Capacidade:", cap)
        print("Valor ótimo esperado:", esperado, "\n")

        # Executa todas as estratégias
        g_choose, g_val = greedy_knapsack(projs, cap)
        r_val = recursive_knapsack(projs, cap)
        m_val = memoized_knapsack(projs, cap)
        dp_val = bottom_up_knapsack(projs, cap)

        print("Gulosa:")
        print("  Selecionados:", g_choose)
        print("  Valor:", g_val)

        print("Recursiva pura:")
        print("  Valor:", r_val)

        print("Top-Down (memo):")
        print("  Valor:", m_val)

        print("Bottom-Up (DP):")
        print("  Valor:", dp_val)

        # Verificação
        if m_val == dp_val == esperado:
            print("-> DP OK")
        else:
            print("-> ERRO: DP não bate com o esperado")

        if g_val < esperado:
            print("-> Gulosa falhou (como esperado em alguns casos).")

    print("\n===== FIM DO PROGRAMA =====")

    # ------------------ ANÁLISE TEÓRICA DE COMPLEXIDADE ------------------
    print("===== ANÁLISE TEÓRICA DAS ESTRATÉGIAS =====\n")

    print("1) Estratégia Gulosa (Greedy Valor/Hora):")
    print("   - Ordenação por razão V/E: O(n log n)")
    print("   - Seleção linear: O(n)")
    print("   - Complexidade total: O(n log n)")
    print("   - Vantagem: Muito rápida.")
    print("   - Desvantagem: Não garante solução ótima para 0/1 knapsack.\n")

    print("2) Solução Recursiva Pura (Exponencial):")
    print("   - Explora todas as combinações possíveis de itens.")
    print("   - Número de subconjuntos: 2^n")
    print("   - Complexidade de tempo: O(2^n)")
    print("   - Complexidade de espaço: O(n) pela profundidade da recursão")
    print("   - Desvantagem: Completamente impraticável para n > 30.\n")

    print("3) Programação Dinâmica Top-Down (Memoização):")
    print("   - Cada subproblema (i, c) é resolvido apenas uma vez.")
    print("   - Tabela de memoização com n * C estados.")
    print("   - Tempo: O(n * C)")
    print("   - Espaço: O(n * C)")
    print("   - Vantagem: Muito mais rápida que a recursão pura.")
    print("   - Observação: Mantém estrutura recursiva, fácil de entender.\n")

    print("4) Programação Dinâmica Bottom-Up (Iterativa):")
    print("   - Preenche tabela (n+1) x (C+1).")
    print("   - Tempo: O(n * C)")
    print("   - Espaço: O(n * C) (pode ser otimizado para O(C))")
    print("   - Vantagem: Solução clássica mais eficiente e confiável.\n")

    print("===== CONCLUSÃO =====")
    print("• A recursão pura é a única exponencial — usada apenas para fins didáticos.")
    print("• A gulosa é rápida, mas não garante ótimo (como mostrado no Caso 2).")
    print("• As soluções de PD Top-Down e Bottom-Up sempre retornam o valor ótimo.")
    print("• Para problemas reais de knapsack 0/1, Bottom-Up ou Top-Down são as melhores escolhas.")
