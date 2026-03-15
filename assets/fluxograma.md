# Fluxograma de Integração: SQL, PHP e Python

```mermaid
graph TD
    A[Usuário/Terminal] -->|Comandos SQL| B[(estudos.db)]
    B -->|Consulta SQL| C[Script PHP]
    B -->|Consulta SQL| D[Script Python]
    C -->|Resultado| E[Exibição no Terminal]
    D -->|Resultado| F[Exibição no Terminal]
```

## Descrição do Fluxo
1. **Banco de Dados (SQL):** Centraliza as informações dos alunos no arquivo `estudos.db`.
2. **PHP:** Conecta ao SQLite, executa a consulta e exibe os dados.
3. **Python:** Conecta ao SQLite nativamente, executa a consulta e exibe os dados.
4. **Integração:** Ambas as linguagens leem a mesma fonte de dados, garantindo consistência.
