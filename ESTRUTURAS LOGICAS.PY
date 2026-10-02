print("Quilão do Allanzão")
preco_quilo = float(input("Digite o preço do quilo:"))
peso_prato = (float(input("Informe o peso do prato do cliente (em kg): ")))

preco_prato = preco_quilo * peso_prato

print(f"O preço do prato do cliente é: R${preco_prato:.2f}")  # O F serve para trazer uma variavel para dentro da string

if peso_prato > 1:
    print("O prato do cliente está acima do peso permitido.Pague um valor fixo de R$ 80,00")
else:
 print("O prato do cliente está dentro do peso permitido. Pague o valor normal.")


