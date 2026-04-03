# --- EXERCÍCIO DE FIXAÇÃO: SISTEMA DE SEGURANÇA HACKER ---

# 1. O BANCO DE DADOS (Dicionário)
# Aqui guardamos quem é o usuário e qual o "poder" (nível) dele.
niveis = {"usuario": "admin", "nivel": 10}

# 2. A MÁQUINA DE SEGURANÇA (Função)
# Esta máquina recebe um perfil e decide se o acesso é permitido.
def checar_acesso(perfil):
    # O "Portão de Segurança" (Decisão)
    if perfil["nivel"] >= 5:
        # Se for nível 5 ou mais, o "túnel" f"..." cria a mensagem de sucesso.
        # Note o uso de 'usuario' com aspas simples dentro das aspas duplas.
        return f"Acesso Concedido, {perfil['usuario']}!"
    else:
        # Se for menor que 5, o "Plano B" é ativado.
        return "Acesso Negado!"

# 3. O MOMENTO DA VERDADE (Chamada e Exibição)
# Pegamos o resultado da máquina e guardamos na etiqueta 'mensagem'.
mensagem = checar_acesso(niveis)

# Gritamos o resultado final na tela.
print(mensagem) 
