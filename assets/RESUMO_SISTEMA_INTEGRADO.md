# Resumo de Progresso: Integração de Sistemas e Banco de Dados

## 1. Banco de Dados (SQL)
- **SQLite:** Banco de dados em arquivo local (`.db`). Ideal para estudos e aplicações leves.
- **MySQL/MariaDB:** Banco de dados cliente-servidor (XAMPP). Ideal para aplicações Web.
- **Operações CRUD:**
    - `CREATE`: Criar tabelas.
    - `INSERT`: Inserir registros.
    - `SELECT`: Consultar dados (uso de `WHERE`, `ORDER BY`, `LIKE`, `BETWEEN`).
    - `UPDATE`: Atualizar registros existentes.
    - `DELETE`: Remover registros.

## 2. Modelagem de Dados (MER/DER)
- **MER (Modelo):** Descrição lógica e textual das regras de negócio.
- **DER (Diagrama):** Representação gráfica (Entidades, Atributos e Relacionamentos).
- **Chave Primária (PK):** Identificador único de um registro.
- **Chave Estrangeira (FK):** Referência que liga uma tabela a outra.
- **JOINs:**
    - `INNER JOIN`: Apenas registros com correspondência em ambos os lados.
    - `LEFT JOIN`: Todos da esquerda + correspondentes da direita.

## 3. Integração com Linguagens
- **PHP:** 
    - Conexão SQLite: `new SQLite3()`.
    - Conexão MySQL: `new mysqli()`.
    - Execução via Terminal (CLI) ou via Servidor Web (Apache/XAMPP).
- **Python:**
    - Conexão nativa via `sqlite3`.
    - Processamento lógico de dados (Cálculos de médias, status e filtros).

## 4. Ambiente de Desenvolvimento
- **XAMPP:** Pacote com Apache (Web), MySQL (Banco) e PHP.
- **phpMyAdmin:** Ferramenta visual para gerenciar MySQL.
- **Git:** Controle de versão e organização de subpastas (`dev-log`).
