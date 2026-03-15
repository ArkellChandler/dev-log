# 🗄️ Estudos de Banco de Dados (SQL)

Este caderno contém a teoria fundamental sobre bancos de dados relacionais e a linguagem SQL.

## 1. O que é SQL?
SQL (**Structured Query Language**) é a linguagem padrão para interagir com Bancos de Dados Relacionais. Com ela, podemos criar tabelas, inserir, consultar, atualizar e excluir dados.

## 2. Conceitos Fundamentais
*   **Banco de Dados:** Coleção organizada de informações.
*   **Tabela:** Conjunto de dados organizados em colunas e linhas.
*   **Coluna (Campo):** Define o tipo de dado (ex: Nome, Idade).
*   **Linha (Registro):** Uma entrada individual de dados na tabela.
*   **Chave Primária (PK):** Um identificador único para cada linha (ex: ID).

## 3. Tabela Comparativa: SQL vs NoSQL

| Característica | SQL (Relacional) | NoSQL (Não Relacional) |
| :--- | :--- | :--- |
| **Estrutura** | Tabelas fixas (Rígido) | Documentos, Grafos, Chaves (Flexível) |
| **Linguagem** | SQL | Variável (JSON, CQL, etc) |
| **Escalabilidade** | Vertical (Aumenta o hardware) | Horizontal (Aumenta o número de servidores) |
| **Uso Ideal** | Transações complexas e consistência | Grandes volumes de dados e flexibilidade |

## 4. Tipos de Comandos SQL
*   **DDL (Data Definition Language):** Define a estrutura (CREATE, DROP, ALTER).
*   **DML (Data Manipulation Language):** Manipula os dados (INSERT, UPDATE, DELETE).
*   **DQL (Data Query Language):** Consulta os dados (SELECT).
