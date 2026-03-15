# --- ESTUDO DE COLEÇÕES EM PYTHON: LISTA VS TUPLA ---

# 1. TUPLA (Imutável - Não muda)
# Usamos para dados que são fixos por natureza.
# O computador processa mais rápido e protege contra erros.
dias_semana = (
    "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"
)

# 2. LISTA (Mutável - Pode mudar)
# Usamos para dados que crescem ou diminuem ao longo do tempo.
historico_temperaturas = [22.5, 23.0, 21.8, 24.5]

# --- TESTE DE COMPORTAMENTO ---

# Adicionando uma nova temperatura à LISTA (Funciona ✅)
historico_temperaturas.append(25.1)
print(f"Histórico Atualizado: {historico_temperaturas}")

# Tentar mudar o primeiro dia da semana na TUPLA (Daria ERRO ❌)
# dias_semana[0] = "Novo Dia" 

# --- RESUMO PARA CONSULTA ---
# [] LISTA: Dinâmica, editável, para inventários e históricos.
# () TUPLA: Estática, travada, para dias, coordenadas e constantes.
