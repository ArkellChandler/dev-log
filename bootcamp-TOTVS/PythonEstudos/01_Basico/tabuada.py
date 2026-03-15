import time # Uma biblioteca para dar um "delay" de 1 segundo

print("--- PREPARAR PARA O LANÇAMENTO ---")

# Começa no 10, para antes do -1, descendo de 1 em 1
for segundo in range(10, -1, -1):
    print(f"Faltam {segundo} segundos...")
    time.sleep(1) # O programa espera 1 segundo antes da próxima volta

print("🚀 DECOLAR!!!")
