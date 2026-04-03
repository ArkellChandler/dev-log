# 💰 Agente Financeiro Inteligente (AI-Driven Fintech Agent)

Sistema consultivo de planejamento financeiro que utiliza **IA Generativa (Gemini)** integrada a uma base de dados proprietária para fornecer conselhos personalizados e seguros.

## ⚙️ Fluxo de Operação (RAG Architecture)
```mermaid
graph TD
    User([Cliente]) -->|Pergunta| App[Interface Streamlit]
    App -->|Input| Agent[Agent Logic]
    Agent -->|Query| DB[(Base de Conhecimento)]
    DB -->|CSV/JSON Data| Agent
    Agent -->|Context + Prompt| Gemini{Gemini 1.5 Flash}
    Gemini -->|Resposta Consultiva| Agent
    Agent -->|Exibição| User
    style DB fill:#050505,stroke:#00f3ff,color:#00f3ff
    style Gemini fill:#050505,stroke:#ff00ff,color:#ff00ff
    style User fill:#050505,stroke:#39ff14,color:#39ff14
```

## 📂 Estrutura do Projeto
- `data/`: Transações (CSV), Perfil (JSON), Produtos (JSON).
- `src/`: Lógica de integração e anti-alucinação (`agent.py`).
- `app.py`: Interface de chat interativa em Streamlit.

## 🛡️ Segurança e Anti-Alucinação
O agente utiliza a técnica de **Context Injection** (RAG simplificado), onde os dados reais do cliente são injetados no prompt do sistema antes da chamada à API. Isso garante que o modelo:
1. Nunca invente valores de saldo ou transações inexistentes.
2. Sugira apenas produtos financeiros presentes no catálogo mockado.
3. Responda "Informação não disponível" para solicitações fora do escopo (ex: Criptoativos).

## 🚀 Como Executar
1. Instale as dependências: `pip install streamlit google-generativeai pandas`
2. Navegue até a pasta: `cd dev-log/projetos/agente_financeiro`
3. Execute a aplicação: `streamlit run app.py`
4. Insira sua **Gemini API Key** no painel lateral do navegador.

---
*C:\Users\User\dev-log\projetos\agente_financeiro> agent status --active*
🟢 **Core: Operational** | **Consultancy: Enabled**
