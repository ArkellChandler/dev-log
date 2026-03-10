# Lista de tecnologias que um Analista de Sistemas usa
tecnologias = ["Python", "SQL", "PowerShell", "Git", "Docker"]

# Nome do arquivo que vamos gerar
nome_arquivo = "lista_tecnologias.txt"

print(f"Iniciando a gravação no arquivo: {nome_arquivo}")

# O comando 'with' garante que o arquivo seja fechado automaticamente
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for item in tecnologias:
        # Escreve o item e pula uma linha (\n)
        arquivo.write(item + "\n")

print("✅ Gravação concluída com sucesso!")
