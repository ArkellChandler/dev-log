-- ==========================================
-- SETUP: REDE FANTASMA (SIMULAÇÃO HACKER)
-- DATA: 2026-03-14
-- ==========================================

-- 1. Tabela de Alvos (Servidores)
CREATE TABLE IF NOT EXISTS alvos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    ip_externo TEXT UNIQUE,
    nivel_seguranca INTEGER,
    recompensa_bitcoin REAL
);

-- 2. Tabela de Operadores (Hackers)
CREATE TABLE IF NOT EXISTS operadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codinome TEXT UNIQUE,
    especialidade TEXT,
    reputacao INTEGER DEFAULT 0
);

-- 3. Tabela de Logs de Ataque
CREATE TABLE IF NOT EXISTS logs_ataque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alvo_id INTEGER,
    operador_id INTEGER,
    status TEXT, -- 'Sucesso' ou 'Falha'
    data_ataque TEXT,
    FOREIGN KEY (alvo_id) REFERENCES alvos(id),
    FOREIGN KEY (operador_id) REFERENCES operadores(id)
);

-- INSERÇÃO DE DADOS (PSEUDODADOS)
INSERT INTO alvos (servidor, ip_externo, nivel_seguranca, recompensa_bitcoin) VALUES 
('Banco Central S.A', '192.168.50.1', 5, 2.5),
('Portal do Governo', '200.15.32.10', 4, 1.2),
('Email Corporativo', '10.0.0.5', 2, 0.3),
('Servidor de Arquivos', '172.16.254.1', 3, 0.8);

INSERT INTO operadores (codinome, especialidade, reputacao) VALUES 
('Shadow', 'Invasão de Rede', 100),
('Ghost', 'Criptografia', 85),
('ZeroOne', 'Engenharia Social', 90);

INSERT INTO logs_ataque (alvo_id, operador_id, status, data_ataque) VALUES 
(3, 1, 'Sucesso', '2026-03-10'),
(2, 2, 'Falha', '2026-03-12'),
(4, 3, 'Sucesso', '2026-03-14');
