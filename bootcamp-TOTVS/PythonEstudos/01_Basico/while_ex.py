# 1. Primeira entrada (Transforma em número)
numero = int(input("Digite um numero negativo para parar: "))

# 2. Enquanto o número for maior ou igual a 0 (ou seja, positivo)
while numero >= 0:
    print(f"O numero {numero} NAO e negativo! Tente de novo.")
    
    # 3. MUDANÇA: Precisamos do int() aqui também!
    numero = int(input("Digite um numero: "))
    
    print(f"Voce digitou: {numero}")

# 4. Só chega aqui se o numero for menor que 0
print(f"BOA! Voce digitou {numero} e o programa parou.")
