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

## 🛠️ Funcionalidades Recentes
- **Gerenciamento de Modelos:** Interface para listar modelos ativos e selecionar dinamicamente entre as versões Gemini 1.5, 2.0 e 2.5.
- **Tratamento de Cota:** Notificação amigável ao usuário caso o limite de requisições da API Gemini (`ResourceExhausted`) seja atingido.
- **Compatibilidade de Dados:** Correção na leitura de arquivos CSV e JSON para suportar codificações com BOM (Byte Order Mark), garantindo estabilidade no Windows.

## 🚀 Como Executar
1. Instale as dependências: `pip install streamlit google-generativeai pandas`
2. Navegue até a pasta: `cd dev-log/projetos/agente_financeiro`
3. Execute a aplicação: `streamlit run app.py`
4. Configure sua Gemini API Key no menu lateral (ou utilize a chave padrão configurada).
5. Selecione o modelo desejado (ex: `gemini-2.0-flash`).
6. Inicie a conversa no chat.

## 📂 Estrutura do Projeto
- `data/`: Transações (CSV), Perfil (JSON), Produtos (JSON).
- `src/`: Lógica de integração e anti-alucinação (`agent.py`).
- `app.py`: Interface de chat interativa em Streamlit.

---
*C:\Users\User\dev-log\projetos\agente_financeiro> agent status --active*
🟢 **Core: Operational** | **Consultancy: Enabled**
