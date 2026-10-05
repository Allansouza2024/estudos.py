print("Saldao do Allanzão")
total_compra = float(input("Digite o valor total da compra:"))
forma_pagamento = int(input("Digite a forma de pagamento (1 - pix, 2 - cartão de crédito, 3 - cartão de débito): "))

if forma_pagamento == 1:
    desconto = total_compra * 0.05
    valor_final = total_compra - desconto
    print(f"O valor da compra foi de R${total_compra:.2f}. Com o desconto de 5% no pixe, o valor final é R${valor_final:.2f}")

elif forma_pagamento == 2:
    parcelas = int(input("Digite o número de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"O valor da compra foi de R${total_compra:.2f}. Com o parcelamento em {parcelas}x, o valor de cada parcela é R${valor_parcela:.2f}")

elif forma_pagamento == 3:
    print(f"O valor da compra foi de R${total_compra:.2f}. Pagamento em cartão de débito.")
else:
    print("Forma de pagamento inválida.")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
# EXERCICIO 1 --
print("Classificação de idade")

idade = int(input("Digite sua idade: "))

if idade <12:
    print("Você é uma criança.")
elif idade >= 12 and idade < 18:
    print("Você é um adolescente.")
elif idade >= 18 and idade <=59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#EXERCICIO 2 --
print("Notas e frequencias escolares")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência escolar (em %): "))


media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
    print(f"Parabéns! Você foi aprovado com média {media:.2f} e frequência de {frequencia:.2f}%")
elif media >= 5 and frequencia >= 75:
    print(f"Você está de recuperação com média {media:.2f} e frequência de {frequencia:.2f}%")
elif media < 5 and frequencia >= 75:
    print(f"Você foi reprovado por nota, com a media {media:.2f} e frequência de {frequencia:.2f}%")
else:
    print(f"Você foi aprovado com a media de {media:.2f}, mas por frequência foi reprvado com {frequencia:.2f}%")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

print("Senha do cofre")

senha_correta = "1234"
tentativa = 0

while tentativa < 3:
    senha_digitada = input("Digite a senha do cofre: ")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso permitido.")
        break
    elif senha_digitada != senha_correta:
        tentativa += 1
        tentativa_restante = 3 - tentativa
        if tentativa_restante > 0:
            print(f"Senha incorreta! Você tem {tentativa_restante} tentativa(s) restante(s).")
        elif tentativa_restante == 0:
            print("Senha incorreta! Você excedeu o número máximo de tentativas. Acesso negado.")
