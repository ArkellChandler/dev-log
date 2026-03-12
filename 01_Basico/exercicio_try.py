hardware = ["SSD", "RAM", "CPU"]
data_registro = "07/03/26"
hardware_list = "lista_hardware.txt"

try:
    with open(hardware_list, "a", encoding="utf-8") as arquivo:
        for item in hardware:
            arquivo.write(f"{item} - Recebido em {data_registro}\n")
    print("✅ Estoque atualizado com sucesso!")
except Exception as e:
    print(f"❌ Ocorreu um erro ao salvar o estoque: {e}")
