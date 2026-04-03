total_pecas = 0
for i in range(5):
    qtd = int(input(f"Digite a quantidade da peça {i+1}: "))
    total_pecas += qtd # O += soma o novo valor ao antigo
print(f"O total de peças no estoque é: {total_pecas}")
