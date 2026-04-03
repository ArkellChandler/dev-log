CREATE DATABASE IF NOT EXISTS db_integracao;
USE db_integracao;

CREATE TABLE IF NOT EXISTS vendas_origem (
    id INT PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    status_sync VARCHAR(20) DEFAULT 'pendente'
);

INSERT INTO vendas_origem (produto, valor) VALUES 
('Placa de Vídeo RTX', 3500.00),
('Processador Ryzen 7', 1800.50),
('Memória RAM 16GB', 450.00),
('SSD NVMe 1TB', 620.00);
