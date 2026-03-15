saldo_final = 0 # Começa em zero para somar

for i in range(3):
    movimentacao = float(input(f"Digite o valor {i+1} (ex: 100 ou -50): "))
    saldo_final += movimentacao # Soma o valor ao saldo atual

# Decisão baseada no resultado final
if saldo_final >= 0:
    print(f"💰 Lucro: R$ {saldo_final:.2f}")
else:
    print(f"📉 Prejuízo: R$ {saldo_final:.2f}")
