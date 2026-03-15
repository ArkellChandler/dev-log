# 🗄️ Estudos de SQL (Structured Query Language)

Este diretório é dedicado ao aprendizado de bancos de dados relacionais e prática de comandos SQL.

## 🛠️ Como Executar os Estudos
Estamos utilizando o **SQLite** para praticar via PowerShell, pois ele é leve e não exige instalação de servidor.

### 1. Criar e Acessar o Banco de Dados
No PowerShell, dentro desta pasta:
```powershell
sqlite3 estudos.db
```

### 2. Comandos do SQLite (Meta-comandos)
Estes comandos começam com ponto (`.`) e servem para controlar o terminal do SQLite:
- `.tables` : Lista todas as tabelas criadas.
- `.schema nome_tabela` : Mostra a estrutura da tabela.
- `.header on` : Mostra os nomes das colunas nos resultados.
- `.mode column` : Formata a saída em colunas organizadas.
- `.exit` : Sai do terminal SQLite.

## 📝 Comandos SQL Básicos (Sintaxe)
**IMPORTANTE:** Todos os comandos SQL devem terminar com `;` (ponto e vírgula).

### DDL (Definição - Estrutura)
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE
);
```

### DML (Manipulação - Dados)
```sql
-- Inserir dados
INSERT INTO usuarios (nome, email) VALUES ('Arkell', 'arkell@exemplo.com');

-- Consultar dados
SELECT * FROM usuarios;

-- Atualizar dados
UPDATE usuarios SET nome = 'Arkell Chandler' WHERE id = 1;

-- Deletar dados
DELETE FROM usuarios WHERE id = 1;
```
