Artificial-Intelligence-Fundamentals

Trabalho de Artificial Intelligence Fundamentals Rota Inteligente: Otimização de Entregas com IA

Descrição do Problema
A empresa local Sabor Express enfrenta dificuldades na definição eficiente de rotas de entrega durante horários de pico (almoço e jantar). Atualmente, as rotas são definidas manualmente, com base apenas na experiência dos entregadores.

Isso gera:

Atrasos frequentes

Aumento no consumo de combustível

Percursos ineficientes

Insatisfação dos clientes

O desafio consiste em desenvolver uma solução baseada em Inteligência Artificial para sugerir as melhores rotas e agrupar entregas próximas de forma eficiente.

Objetivos do Projeto
Modelar a cidade como um grafo ponderado

Implementar algoritmos de busca para encontrar o menor caminho

Aplicar clustering (K-Means) para agrupar entregas próximas

Comparar desempenho entre diferentes algoritmos

Avaliar eficiência da solução com métricas quantitativas

Fundamentação Teórica Otimização de Rotas
Inspirado em sistemas reais como o ORION da UPS, que utiliza heurísticas avançadas para reduzir milhões de milhas percorridas anualmente.

O projeto utiliza:

A* (A-Star)

BFS (Busca em Largura)

DFS (Busca em Profundidade)

Agrupamento de Entregas

Utilizamos K-Means para agrupar entregas geograficamente próximas, estratégia semelhante a soluções de empresas como Kardinal.ai.

Cada cluster representa uma zona otimizada de entrega.

Modelagem do Problema
A cidade foi modelada como um grafo ponderado, onde:

Nós → bairros/pontos de entrega

Arestas → ruas

Pesos → distância estimada

Exemplo de representação:

grafo = { "Centro": {"BairroA": 5, "BairroB": 8}, "BairroA": {"Centro": 5, "BairroC": 4}, } 5. Algoritmos Implementados A*

Utiliza custo real + heurística (distância euclidiana)

Mais eficiente em grafos ponderados

Garante o menor caminho se a heurística for admissível

Complexidade aproximada: O(E log V)

BFS

Explora por níveis

Garante menor caminho apenas em grafos não ponderados

Serve como comparação

DFS

Explora profundamente

Não garante menor caminho

Utilizado como baseline

K-Means

Agrupa entregas por proximidade

Reduz deslocamentos longos

Permite dividir trabalho entre entregadores

Resultados Obtidos (Simulação) Algoritmo Distância Total Tempo Execução Nós Visitados DFS 34 km 0.021 s 18 BFS 27 km 0.015 s 12 A* 22 km 0.006 s 7 Redução de 35% na distância comparado ao método manual simulado.
Após aplicação de clustering:

Redução média adicional de 18% na distância total

Melhor balanceamento entre entregadores

Métricas Avaliadas
Distância total percorrida

Tempo computacional

Número de nós visitados

Eficiência comparativa entre algoritmos

Limitações
Não considera trânsito em tempo real

Número fixo de clusters

Não resolve completamente o problema do Caixeiro Viajante (TSP)

Dados simulados

Melhorias Futuras
Integração com API de mapas

Algoritmos Genéticos

Programação Linear Inteira (MILP)

Aprendizado por Reforço

Atualização dinâmica de rotas
