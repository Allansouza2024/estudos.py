# print("Quilão do Allanzão")
# preco_quilo = float(input("Digite o preço do quilo:"))
# peso_prato = (float(input("Informe o peso do prato do cliente (em kg): ")))

# preco_prato = preco_quilo * peso_prato

# print(f"O preço do prato do cliente é: R${preco_prato:.2f}")  # O F serve para trazer uma variavel para dentro da string

# if peso_prato > 1:
#     print("O prato do cliente está acima do peso permitido.Pague um valor fixo de R$ 80,00")
# else:
#     print("O prato do cliente está dentro do peso permitido. Pague o valor normal.")

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------




