# Fluxogramas e Teoria: Ciência de Dados e Nuvem

Este documento detalha os fluxos lógicos e a base teórica para manipulação de dados, aprendizado de máquina e infraestrutura em nuvem.

---

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
- **Pandas:** Biblioteca para manipulação de dados estruturados (DataFrames). A leitura via GitHub exige o link 'raw' para obter o conteúdo puro.
- **Matplotlib (Pyplot):** Interface para criação de gráficos em camadas (eixos, títulos, renderização).

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
- **model.fit(X, y):** Etapa de treinamento onde o modelo aprende a relação entre atributos e alvos.
- **model.predict(X_novo):** Etapa de inferência onde o modelo estima resultados para dados não vistos.

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
- **Idempotência:** No Luigi, se o arquivo de saída (Target) já existe, a tarefa é considerada concluída e não é reexecutada.

---

### 4. Computação em Nuvem: Modelos e Arquiteturas
```mermaid
graph TD
    subgraph "Modelos de Implementação"
        A[On-Premise] --- B[Hybrid Cloud]
        B --- C[Public Cloud]
    end

    subgraph "Modelos de Serviço (As a Service)"
        D[IaaS] --> E[PaaS]
        E --> F[SaaS]
    end

    A1[Você cuida de TUDO] --> A
    D1[Nuvem cuida do Hardware] --> D
    E1[Nuvem cuida do S.O. e Runtime] --> E
    F1[Nuvem cuida do Aplicativo] --> F
```

| Conceito | Analogia | Descrição Técnica |
| :--- | :--- | :--- |
| **On-Premise** | Cozinhar em Casa | Infraestrutura física local. Você é responsável pelo hardware, energia e software. |
| **IaaS** | Alugar a Cozinha | Infraestrutura como Serviço. Você aluga servidores virtuais (EC2) e instala o que desejar. |
| **PaaS** | Pedir um Kit de Cozinha | Plataforma como Serviço. O S.O. e o Python/SQL já estão prontos. Você foca no código. |
| **SaaS** | Comer no Restaurante | Software como Serviço. Aplicação pronta via browser (Office 365, Google Drive). |

---

### 5. Infraestrutura Global AWS
```mermaid
graph TD
    A[AWS Global] --> B[Regiões]
    B --> C[Availability Zones - AZs]
    A --> D[Edge Locations]
    C --> E[Data Centers Físicos]
    D --> F[Route 53 / CloudFront]
```

- **Regiões:** Localidades geográficas isoladas (ex: São Paulo).
- **AZs:** Conjuntos de Data Centers dentro de uma região. Para alta disponibilidade, use pelo menos duas AZs.
- **Edge Locations:** Pontos de presença para entrega de conteúdo com baixa latência (CDN).
