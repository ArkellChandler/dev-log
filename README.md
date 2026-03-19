# 🚀 Dev-Log: Engenharia de Dados & Integração

![DIO](https://img.shields.io/badge/DIO-Open%20Source-ee4d2d?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

Repositório central para documentação e estudos técnicos focados em **Arquitetura de Dados**, **Machine Learning** e **Resiliência de Sistemas**.

---

## 🏗️ Projeto de Destaque: Pipeline ETL & Analytics com Disaster Recovery

Este projeto demonstra um fluxo completo de dados, desde a extração em um banco relacional até a visualização analítica, com camadas de segurança e recuperação.

### 🛠️ Arquitetura da Solução
### 🔄 Fluxo de Dados e Processamento

```mermaid
graph TD
    %% Fontes de Dados
    subgraph "Camada de Dados (XAMPP)"
        DB[(MySQL/MariaDB)] -- "Dados Brutos" --> PY_ETL
    end

    %% Processamento Python
    subgraph "Processamento (Python 3.x)"
        PY_ETL(Script sync_data.py) -- "1. Limpeza/Tipagem (Pandas)" --> PY_ML
        PY_ML(Script sync_data.py) -- "2. Predição (Scikit-Learn)" --> PY_JSON
        PY_JSON(Script sync_data.py) -- "3. Exportação Records" --> ASSETS_DIR
    end

    %% Camada de Recuperação
    subgraph "Resiliência (recovery_manager.py)"
        RECOVERY{Health Check SQL}
        RECOVERY -- "Sucesso" --> CSV_BK[Gera Backup CSV]
        RECOVERY -- "Falha" --> FAILOVER[Ativa Failover]
        FAILOVER -- "Nível 1" --> JSON_DATA
        FAILOVER -- "Nível 2" --> CSV_BK
    end

    %% Interface e Saída
    subgraph "assets/"
        ASSETS_DIR[Diretório de Intercâmbio] --> JSON_DATA[data_sync.json]
        ASSETS_DIR[Diretório de Intercâmbio] --> CSV_BK
    end

    subgraph "Interface (Apache/XAMPP)"
        PHP_DASH(Dashboard PHP) -- "Consome JSON" --> JSON_DATA
        PHP_DASH -- "Renderiza BI" --> CHARTJS[Chart.js / Tabela]
    end

    %% Orquestração
    POWER_SHELL[[PS executar_pipeline.ps1]] -. "Gatilha ETL/ML" .-> PY_ETL

    %% Estilização
    classDef database fill:#f96,stroke:#333,stroke-width:2px;
    classDef process fill:#69c,stroke:#333,stroke-width:1px,color:white;
    classDef storage fill:#ff9,stroke:#333,stroke-width:1px;
    classDef interface fill:#ccf,stroke:#333,stroke-width:1px;
    classDef recovery fill:#f99,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;

    class DB database;
    class PY_ETL,PY_ML,PY_JSON process;
    class JSON_DATA,CSV_BK storage;
    class PHP_DASH,CHARTJS interface;
    class RECOVERY,FAILOVER recovery;
1.  **Camada de Dados:** MySQL (MariaDB) via XAMPP atuando como a fonte transacional de origem.
2.  **Processamento (ETL):** Script Python utilizando **Pandas** para limpeza, tipagem e transformação de dados.
3.  **Machine Learning:** Integração com **Scikit-Learn** para geração de predições e métricas sobre os dados brutos.
4.  **Resiliência (Recovery):** Módulo de recuperação que alterna automaticamente entre SQL, JSON e CSV em caso de falha crítica.
5.  **Interface de BI:** Dashboard dinâmico em PHP consumindo a ponte JSON e renderizando gráficos via **Chart.js**.

---

## 🛡️ Módulo de Recuperação (Disaster Recovery)
O sistema conta com um gerenciador de integridade (`recovery_manager.py`) que opera em três níveis:
- **Nível 1:** Conexão direta com a fonte SQL.
- **Nível 2:** Failover para cache JSON estruturado.
- **Nível 3:** Restauração via Backup CSV de emergência.



---

## 📂 Estrutura das Pastas

### 📁 [machine_learning](machine_learning)
* **`sync_data.py`**: Script principal de integração e transformação.
* **`recovery_manager.py`**: Sistema de monitoramento e recuperação de dados.
* **`dashboard.php`**: Painel visual de acompanhamento.
* **`executar_pipeline.ps1`**: Orquestrador em PowerShell para automação no Windows 11.
* **📁 [assets](assets)**: Arquivos de intercâmbio (JSON/CSV) e logs.

### 📁 [sql](sql)
* Scripts de definição de esquema e carga inicial de dados.

---

## 🛠️ Stack Tecnológica
- **Linguagens:** Python, PHP, PowerShell, SQL.
- **Data Science:** Pandas, Scikit-Learn.
- **Web/BI:** Apache, Chart.js, JSON.
- **Ambiente:** Windows 11 / Debian (WSL).

---
*Este repositório é um registro vivo de evolução técnica e boas práticas em Engenharia de Software.*
