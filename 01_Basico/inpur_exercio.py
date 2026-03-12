carrinho = []

for i in range(3):
    item = input(f"Digite o nome da peça {i+1}: ")
    carrinho.append(item)

try:
    with open("carrinho.txt", "a", encoding="utf-8") as arquivo:
        for item in carrinho:
            arquivo.write(f"{item}\n") 
    print(" Gravado com sucesso!")

except Exception as e:
    print(f" Ocorreu um erro na gravação: {e}")
