import google.generativeai as genai
import datetime

# Configuração da Chave
genai.configure(api_key='AIzaSyDGRW1DTEfh9bu-3UFwr1aI-ihyeamggkE')
model = genai.GenerativeModel('gemini-1.5-flash')

# O que você quer que eu gere?
prompt = "Gere um resumo técnico curto (em Markdown) sobre um conceito de Python ou Redes para um estudante iniciante."

# Gerando o conteúdo
response = model.generate_content(prompt)
materia = response.text

# Criando o nome do arquivo com a data de hoje
data_hoje = datetime.date.today().strftime("%d-%m-%Y")
nome_arquivo = f"estudo_{data_hoje}.md"

# Salvando no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write(f"# Estudo do Dia: {data_hoje}\n\n")
    f.write(materia)

print(f"✅ Matéria gerada com sucesso: {nome_arquivo}")
