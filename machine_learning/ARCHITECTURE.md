# 🗺️ Arquitetura Técnica do Sistema

Este documento detalha o fluxo de dados e a integração entre as tecnologias utilizadas no projeto.

## 🔄 Fluxograma de Dados (Mermaid)

```mermaid
graph TD
    %% Camada de Dados
    subgraph "Camada de Ingestão"
        A[(MySQL / XAMPP)] -->|SQL Query| B(Python ETL)
    end

    %% Camada de Processamento
    subgraph "Camada de Inteligência"
        B -->|Pandas Dataframe| C[Scikit-Learn Model]
        C -->|Predição de Margem| D{JSON Generator}
    end

    %% Camada de Saída
    subgraph "Camada de Apresentação"
        D -->|data_sync.json| E[Dashboard PHP]
        D -->|swagger.json| F[Swagger UI]
    end

    %% Resiliência
    subgraph "Módulo de Recuperação"
        B -.->|Failover| G[Backup CSV]
        G -.->|Restore| D
    end

    %% Estilos
    style A fill:#f96,stroke:#333
    style B fill:#69c,stroke:#333,color:#fff
    style C fill:#69c,stroke:#333,color:#fff
    style E fill:#ccf,stroke:#333
    style F fill:#85ea2d,stroke:#333
