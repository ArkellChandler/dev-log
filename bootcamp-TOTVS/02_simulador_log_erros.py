historico = []

for i in range(3):
    # O input e o append ficam DENTRO do loop (com TAB)
    erro = input(f"Digite o código do erro {i+1}: ")
    historico.append(erro)

print("\n--- Relatório Diário ---")
print(f"Erros registrados hoje: {historico}")

# Verificamos se o erro crítico "500" está na lista
if "500" in historico:
    print("🚨 ALERTA CRÍTICO: Chamar suporte nível 2!")
else:
    print("✅ Sistema estável, sem erros graves.")
