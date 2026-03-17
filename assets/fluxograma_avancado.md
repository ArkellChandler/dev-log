# Fluxograma do Sistema Integrado

```mermaid
graph TD
    subgraph Web_Client
        A[Navegador Chrome/Edge]
    end

    subgraph Server_Side_XAMPP
        B[Apache Server]
        C[PHP MySQL Extension]
        D[phpMyAdmin]
    end

    subgraph Database_Storage
        E[(MySQL/MariaDB)]
        F[(SQLite estudos.db)]
    end

    subgraph Data_Processing_Scripts
        G[Script Python]
        H[Script PHP CLI]
    end

    A -->|URL localhost| B
    B -->|Executa| C
    C -->|Consulta| E
    D -->|Gerencia| E
    G -->|Processa| F
    H -->|Executa| F
    E -->|Resposta| C
    C -->|Gera HTML| B
    B -->|Exibe| A
```

## Fluxo de Dados:
1. **Navegador:** O usuário acessa a página PHP no localhost.
2. **Servidor (Apache/PHP):** Processa o código PHP.
3. **Conector:** O PHP busca dados no banco MySQL (XAMPP).
4. **Retorno:** O PHP envia o HTML final para o navegador.
5. **Automação:** Scripts Python e PHP-CLI operam diretamente nos arquivos SQLite locais.
