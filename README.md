[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArkellChandler/dev-log/blob/main/projetos/machine_learning/notebook_entrega.ipynb)

# 🌐 DECODER_PROJECT: Dev-Log & Data Architecture
### *“O futuro já chegou, só não foi distribuído uniformemente.”*

![Status](https://img.shields.io/badge/System_Status-Online-00f3ff?style=for-the-badge&logo=target)
![TOTVS](https://img.shields.io/badge/TOTVS_Bootcamp-Concluido-ff00ff?style=for-the-badge)
![Accenture](https://img.shields.io/badge/Accenture_Python-In_Progress-f3f315?style=for-the-badge&logo=python)
![Language](https://img.shields.io/badge/Stack-Python_%7C_SQL_%7C_PHP-39ff14?style=for-the-badge)

---

## 🎓 Formação & Bootcamps (Upgrade Progress)

- **[SUCCESS]** 🚀 **TOTVS Bootcamp** | [Acessar Pasta](./bootcamps/totvs)
- **[LOADING]** 🐍 **Accenture** | [Acessar Pasta](./bootcamps/accenture)
- **[NEW]** 📓 **DIO Challenge** | [Miniguia de Estudos: NotebookLM](./desafios/notebooklm)

### 📊 Status de Evolução Técnica (Study Progress)
| Bootcamp / Skill | Status | Barra de Progresso |
| :--- | :--- | :--- |
| **TOTVS (Data Eng)** | `SUCCESS` | ![100%](https://geps.dev/progress/100?dangerColor=00f3ff&warningColor=ff00ff&successColor=39ff14) |
| **Accenture (Python)** | `LOADING` | ![45%](https://geps.dev/progress/45?dangerColor=00f3ff&warningColor=ff00ff&successColor=f3f315) |
| **Anki (Sintaxe/Teoria)** | `ACTIVE` | ![80%](https://geps.dev/progress/80?dangerColor=00f3ff&warningColor=ff00ff&successColor=00f3ff) |

### 🚀 Roadmap de Conhecimento (Learning Flow)
```mermaid
graph TD
    A[Caderno de Estudos .txt] -->|Curadoria| B(Anki: Flashcards Cyberpunk)
    B -->|Prática de Comandos| C{Scripts de Automação}
    C -->|Fintech ML| D2[Fraud Detection System]
    C -->|Python/Pandas| D[Bootcamp Accenture]
    C -->|SQL/ETL| E[Bootcamp TOTVS]
    D2 -->|Modelagem| F[Dev-Log: Repositório Central]
    D -->|Integração| F
    E -->|Resiliência| F
    style A fill:#050505,stroke:#00f3ff,stroke-width:2px,color:#00f3ff
    style B fill:#050505,stroke:#ff00ff,stroke-width:2px,color:#ff00ff
    style C fill:#050505,stroke:#f3f315,stroke-width:2px,color:#f3f315
    style D2 fill:#050505,stroke:#ff0000,stroke-width:2px,color:#ff0000
    style F fill:#050505,stroke:#39ff14,stroke-width:4px,color:#39ff14
```

---

## 🏗️ Projetos de Destaque (System Architecture)

### 🛡️ I. Fraud Detection System (Fintech Solution)
*Sistema de Monitoramento e Inteligência para Detecção de Fraudes Financeiras*

![XGBoost](https://img.shields.io/badge/Model-XGBoost-ff00ff?style=flat-square&logo=python)
![F1-Score](https://img.shields.io/badge/F1--Score-1.00-39ff14?style=flat-square)

1. **Arquitetura:** Engine modular com `data_loader`, `models` e `train_pipeline`.
2. **Algoritmo:** Classificador XGBoost otimizado para dados imbalanced.
3. **Métricas:** Geração automática de Matriz de Confusão e Relatórios Técnicos.
4. **Localização:** [Acessar Projeto](./projetos/fraud-detection)

### 🛡️ II. Pipeline ETL & Disaster Recovery
*Visualização de Fluxo de Dados e Resiliência em Tempo Real*

1. **Camada de Dados:** MySQL (MariaDB) Transacional.
2. **Processamento:** Pandas Engine para Limpeza e Transformação.
3. **Resiliência:** `recovery_manager.py` (Failover para JSON/CSV).

---

## 📂 Projetos Ativos & Estrutura

### 📁 [bootcamps](./bootcamps)
> Repositório das formações TOTVS e Accenture.

### 📁 [projetos](./projetos)
> Projetos core: Fraud Detection, Machine Learning e SQL Architecture.

### 📁 [desafios](./desafios)
> Desafios de curta duração (Ex: NotebookLM).

### 📁 [recursos](./recursos)
> Materiais de apoio, estudos e o Deck de Flashcards Anki.

---

## 🛠️ Tech Stack: System Components
- **Core:** Python, PHP, SQL, PowerShell.
- **Data Science:** Pandas, Scikit-Learn.
- **Environment:** Windows 11 (HUD Optimized) / WSL2 Debian.

---
*C:\Users\User\dev-log> systemctl status repo_integrity*
🟢 **Active: Operational** | *Last update: Today*
