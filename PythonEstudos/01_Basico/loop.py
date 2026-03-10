# 1. Começamos o loop de 3 voltas
for i in range(3):
    print(f"\n--- Leitura {i + 1} ---")
    
    # 2. A pergunta agora está DENTRO do loop
    # O int() envolve o input() inteiro
    temp = int(input("Qual a temperatura atual?: "))

    # 3. A decisão também está DENTRO do loop (com recuo)
    if temp > 40:
        print("🔥 ALERTA! Cooler ao máximo!")
    else:
        print("✅ Temperatura estável.")

# 4. Fora do loop (sem recuo), o encerramento
print("\nMonitoramento concluído.")
