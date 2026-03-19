# # Dev-Log: Engenharia de Dados & Backend

![DIO](https://img.shields.io/badge/DIO-Open%20Source-ee4d2d?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success?style=for-the-badge)

Repositório central para documentação e estudos técnicos focados em **Integração de Sistemas**, **Arquitetura de Dados** e **Backend**.

---

## 🚀 Projeto de Destaque: Pipeline ETL & Analytics Híbrido
Este repositório contém uma implementação completa de um fluxo de dados (ETL) integrando múltiplas tecnologias para resolver um cenário real de sincronização de dados.

### 🏗️ Arquitetura da Solução
1.  **Camada de Persistência:** MySQL (MariaDB) via XAMPP atuando como banco transacional (ERP).
2.  **Engine de ETL:** Python + Pandas para extração, limpeza e tipagem de dados.
3.  **Inteligência de Dados:** Scikit-Learn para modelagem e predição de margens sobre os dados brutos.
4.  **Camada de Integração:** Exportação estruturada em JSON para garantir o desacoplamento entre o Backend e o Processamento.
5.  **Interface de Analytics:** Dashboard em PHP com visualização gráfica via Chart.js, consumindo dados processados em tempo real.

---

## 📂 Estrutura do Repositório

### 📁 [machine_learning](machine_learning)
* **`sync_data.py`**: Maestro do pipeline (SQL -> Pandas -> ML -> JSON).
* **`dashboard.php`**: Interface de visualização de BI.
* **`executar_pipeline.ps1`**: Script de automação e orquestração para Windows 11.
* **📁 [assets](assets)**: Armazenamento de arquivos de intercâmbio (JSON) e documentação visual.

### 📁 [sql](sql) / [06_MySQL](06_MySQL)
* Modelagem de bancos relacionais e scripts de setup (`setup_db.sql`).

### 📁 [etl](etl) / [pandas](pandas)
* Estudos aprofundados sobre processos de Extração, Transformação e Carga.

---

## 🛠️ Stack Tecnológica
* **Linguagens:** Python 3.x, PHP 8.x, PowerShell, JavaScript
* **Bancos de Dados:** MySQL, MariaDB, SQLite, MongoDB, Redis
* **Ferramentas de Infra:** Git, VS Code, XAMPP, Terminal Linux (Debian)
* **Bibliotecas:** Pandas, Scikit-Learn, Matplotlib, Chart.js

## 🌐 Open Source & Comunidade
* **DIO (Digital Innovation One):** Participação ativa em projetos e ecossistemas de aprendizado open source.

---
*Este repositório serve como portfólio técnico e registro de evolução contínua em Engenharia de Dados.*
