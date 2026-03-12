soma = 0
limite = int(input("Digite um Numero... "))

# Coloquei o ':' no final e o +1 no limite
for i in range(1, limite + 1):
    # Coloquei o ':' no final do if
    if i % 2 == 0:
        # A soma e o print ganharam MAIS UM TAB (estão dentro do if)
        soma = soma + i
        print(f"Achei o par {i}! Total: {soma}")

print(f"Resultado final da soma de pares: {soma}")
