import sys

def main():
    # Lê o valor total da compra a partir da entrada padrão
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        valor = int(input_data)
        
        # Lógica de promoções baseada em regras de negócio
        if valor < 50:
            print("Obrigado por comprar conosco!")
        elif 50 <= valor <= 99:
            print("Parabens! Voce ganhou um brinde!")
        elif 100 <= valor <= 199:
            print("Desconto de 10 reais aplicado!")
        elif valor >= 200:
            print("Desconto de 25 reais aplicado!")
            
    except ValueError:
        pass # Ignora entradas que não sejam números inteiros

if __name__ == "__main__":
    main()
