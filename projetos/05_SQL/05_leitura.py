import sqlite3
import os

# Caminho para o banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'estudos.db')

try:
    # 1. Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 2. Executar a consulta SQL
    cursor.execute("SELECT * FROM alunos")

    # 3. Obter todos os resultados
    alunos = cursor.fetchall()

    print("--- LISTA DE ALUNOS (PYTHON) ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Nota: {aluno[2]}")
    print("--------------------------------")

    # 4. Fechar a conexão
    conn.close()

except sqlite3.Error as e:
    print(f"Erro no SQLite: {e}")
