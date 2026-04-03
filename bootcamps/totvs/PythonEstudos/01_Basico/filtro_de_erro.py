codigo = int(input("Digite o código de erro: "))
if codigo == 404 or codigo == 500:
    print("Erro crítico no servidor!")
elif codigo == 200:
    print("Servidor OK")
else:
    print("Código desconhecido")
