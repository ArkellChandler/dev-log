-- ==========================================
-- EXERCÍCIO 01: CRIAÇÃO E INSERÇÃO
-- OBJETIVO: Criar uma tabela de produtos e popular com dados.
-- DATA: 2026-03-14
-- ==========================================

-- 1. Criar a tabela de produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT,
    preco REAL,
    quantidade INTEGER DEFAULT 0
);

-- 2. Inserir dados de exemplo
INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('Teclado Mecânico', 'Periféricos', 250.00, 10);
INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('Mouse Gamer', 'Periféricos', 150.00, 15);
INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES ('Monitor 24"', 'Hardware', 850.00, 5);

-- 3. Consulta simples para verificar
SELECT * FROM produtos;

-- 4. Consulta com filtro (Preço maior que 200)
SELECT nome, preco FROM produtos WHERE preco > 200;
