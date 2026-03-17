import sqlite3

db_path = r'C:\Users\User\dev-log\05_SQL\estudos.db'

def auditor_de_notas():
    try:
        # 1. Conectar ao banco
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 2. Solicitar o ID do aluno para o usuário
        id_aluno = input("Digite o ID do aluno que deseja auditar: ")

        # 3. Buscar o aluno no banco para confirmar existência
        cursor.execute("SELECT nome, nota FROM alunos WHERE id = ?", (id_aluno,))
        aluno = cursor.fetchone()

        if aluno:
            nome_atual, nota_atual = aluno
            print(f"Aluno encontrado: {nome_atual} | Nota atual: {nota_atual}")

            # 4. Solicitar a nova nota
            nova_nota = float(input(f"Digite a nova nota para {nome_atual}: "))

            # 5. Lógica de Status (Estrutura de Controle if/elif/else)
            if nova_nota >= 9.0:
                novo_status = "EXCELENTE"
            elif nova_nota >= 7.0:
                novo_status = "APROVADO"
            else:
                novo_status = "RECUPERAÇÃO"

            # 6. Atualizar o banco de dados (UPDATE)
            cursor.execute("UPDATE alunos SET nota = ?, status = ? WHERE id = ?", (nova_nota, novo_status, id_aluno))
            conn.commit()
            print(f"Sucesso! {nome_atual} agora está com status: {novo_status}")

        else:
            print("Erro: Aluno não encontrado com este ID.")

        conn.close()

    except ValueError:
        print("Erro: Por favor, digite apenas números para o ID e para a Nota.")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

if __name__ == "__main__":
    auditor_de_notas()
