senha_correta = "ADS2026"
for i in range(3):
    usuario = input("Digite seu nome: ")
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada == senha_correta:
        print("Bem-vindo, " + usuario)
        break # Sai do loop se acertar
    else:
        print("Senha incorreta!")
else:
    # Este 'else' do for roda se o loop terminar sem o break (acabar as 3 chances)
    print("Usuário bloqueado permanentemente.")
