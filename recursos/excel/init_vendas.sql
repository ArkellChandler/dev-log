-- Criação da Tabela de Vendas
CREATE TABLE Vendas_Desafio (
    ID_Venda INT PRIMARY KEY,
    Data_Venda DATE,
    Produto VARCHAR(50),
    Regiao VARCHAR(50),
    Quantidade INT,
    Valor_Unitario DECIMAL(10,2),
    Total AS (Quantidade * Valor_Unitario) -- Coluna calculada
);

-- Inserção de Dados (Amostra para o Dashboard)
INSERT INTO Vendas_Desafio (ID_Venda, Data_Venda, Produto, Regiao, Quantidade, Valor_Unitario)
VALUES 
(1, '2026-01-05', 'Monitor 24', 'São Paulo', 2, 800.00),
(2, '2026-01-12', 'Mouse Gamer', 'Curitiba', 5, 200.00),
(3, '2026-01-20', 'Cadeira Office', 'Rio de Janeiro', 1, 1200.00),
(4, '2026-02-02', 'Teclado Mecânico', 'São Paulo', 3, 350.00),
(5, '2026-02-15', 'Headset 7.1', 'Belo Horizonte', 4, 250.00),
(6, '2026-02-28', 'Monitor 24', 'Rio de Janeiro', 1, 800.00),
(7, '2026-03-05', 'Mouse Gamer', 'São Paulo', 10, 200.00);
