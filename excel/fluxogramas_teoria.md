# Fluxogramas e Teoria do Projeto de Vendas

### 1. Manipulação e Visualização (Pandas & Matplotlib)
```mermaid
graph TD
    A[Início: Script Python] --> B[Importação: pandas e matplotlib]
    B --> C{Origem do Dado?}
    C -->|GitHub / Web| D[Link URL formato raw]
    C -->|Local| E[Caminho do Arquivo]
    D --> F[Leitura: pd.read_csv / pd.read_excel]
    E --> F
    F --> G[Limpeza e Inspeção: df.head / df.info / df.dropna]
    G --> H[Transformação: df.groupby / Agregações]
    H --> I[Visualização: plt.plot / plt.bar / plt.scatter]
    I --> J[Exibição: plt.show]
```
**Teoria:**
- **Pandas:** É uma biblioteca para manipulação e análise de dados estruturados. O objeto principal é o `DataFrame` (tabela bidimensional). A leitura de dados via URL (GitHub) requer o link no formato 'raw' para que o interpretador receba o conteúdo textual puro do arquivo.
- **Matplotlib (Pyplot):** É uma interface de plotagem que permite criar gráficos de forma sequencial. O comando `plt.plot()` define os eixos e o tipo de gráfico, enquanto `plt.show()` renderiza o resultado final na tela.

---

### 2. Machine Learning - Predição (Scikit-Learn)
```mermaid
graph LR
    A[DataFrame Original] --> B[Separação: X Atributos e y Alvo]
    B --> C[Divisão: Treino e Teste]
    C --> D[Instanciação: model = Algoritmo]
    D --> E[Treinamento: model.fit X_train, y_train]
    E --> F[Modelo Treinado]
    F --> G[Inferência: model.predict X_test]
    G --> H[Avaliação: Previsões vs y_test]
```
**Teoria:**
- **model.fit(X, y):** Este método executa o treinamento do algoritmo. O parâmetro `X` representa a matriz de características (atributos) e `y` o vetor de alvos (o que se deseja prever). O modelo busca padrões matemáticos que correlacionam `X` com `y`.
- **model.predict(X_novo):** Após o treinamento, o modelo utiliza os padrões aprendidos para estimar resultados em dados que ele ainda não viu. É a etapa de inferência estatística.

---

### 3. Pipeline de Dados (Luigi Framework)
```mermaid
graph TD
    A[Execução da Task] --> B{O Target do output existe?}
    B -- Sim --> C[Task Completa: Nada a fazer]
    B -- Não --> D[Chamada de requires]
    D --> E[Execução Recursiva das Dependências]
    E --> F[Execução do método run]
    F --> G[Criação do Target de saída]
    G --> H[Conclusão da Task]
```
**Teoria:**
- **Task:** A unidade básica de trabalho no Luigi. Cada tarefa deve ser atômica e específica.
- **requires():** Define o grafo de dependências. Uma tarefa só executa se todas as suas dependências estiverem concluídas.
- **output() / Target:** O Luigi é baseado em "Targets" (alvos). Se o arquivo definido no `output()` (geralmente um `LocalTarget`) já existir no disco, o Luigi entende que a tarefa já foi realizada e não a executa novamente, garantindo a eficiência do pipeline (idempotência).
- **run():** Contém a lógica de processamento dos dados.
