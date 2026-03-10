senha_mestra = "admin123"

# O range(3) abre o ciclo de 3 voltas
for i in range(3):
    print(f"\n--- Tentativa {i + 1} de 3 ---")
    
    # O input precisa estar dentro do loop para perguntar de novo
    tentativa = input("Digite sua senha: ")

    if tentativa == senha_mestra:
        print("✅ Acesso permitido ao sistema!")
        break # O 'break' para o loop se ele acertar de primeira
    else:
        print("❌ Senha incorreta.")

print("\nProcesso finalizado.")
