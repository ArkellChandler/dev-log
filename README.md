# 🚀 Dev-Log: Engenharia de Dados & Integração

![DIO](https://img.shields.io/badge/DIO-Open%20Source-ee4d2d?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

Repositório central para documentação e estudos técnicos focados em **Arquitetura de Dados**, **Machine Learning** e **Resiliência de Sistemas**.

---

## 🏗️ Projeto de Destaque: Pipeline ETL & Analytics com Disaster Recovery

Este projeto demonstra um fluxo completo de dados, desde a extração em um banco relacional até a visualização analítica, com camadas de segurança e recuperação.

### 🛠️ Arquitetura da Solução
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
