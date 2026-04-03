soma_notas = 0 # Iniciamos o acumulador em zero

for i in range(3):
    # Pedimos a nota e já convertemos para float (para aceitar notas tipo 7.5)
    nota = float(input(f"Digite a nota {i + 1}: "))
    
    # Soma a nota atual ao total que já tínhamos
    soma_notas += nota 

# Agora, fora do loop, calculamos a média
media = soma_notas / 3

print(f"Sua média final foi: {media:.2f}")

# Decisão de aprovação
if media >= 7:
    print("✅ Aluno aprovado")
else:
    print("❌ Aluno reprovado")
