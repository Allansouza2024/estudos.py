senha = 4321
senha_digitada = int(input("Digite a senha do cofre: "))
tentativa = 0

while senha_digitada != senha:
    print("Senha incorreta! Tente novamente.")
    senha_digitada = int(input("Digite a senha do cofre: "))
    print("Você tem 3 tentativas para acertar a senha.")

    tentativa += 1
    if tentativa <3:
         


    

