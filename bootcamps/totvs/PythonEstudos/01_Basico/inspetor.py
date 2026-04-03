defeitos = [] # Lista começa vazia

for i in range(4):
    peca = input(f"Digite o nome da peça {i+1}: ")
    status = input(f"A peça '{peca}' está com defeito? (sim/nao): ")
    
    if status == "sim":
        defeitos.append(peca) # Guardamos o NOME da peça com defeito
        print("Registrado no sistema de manutenção.")

# Fora do loop, mostramos o resumo
print(f"\nTotal de peças com defeito: {len(defeitos)}")
print(f"Lista para conserto: {defeitos}")
