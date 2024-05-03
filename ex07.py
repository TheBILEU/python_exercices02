# Para atrair mais clientes, uma loja de roupas oferece um desconto de 5% para quem faz
# compras de R$200,00 ou mais.
# Escreva um programa que leia:
# o preço sem desconto de uma compra.
# Como saída, imprima:
# o valor a ser pago pelo cliente.
# Resultados em moeda devem ser arredondados em duas casas decimais de precisão.

clothesPrice = float(input("Price: "))

if clothesPrice >= 200:
  fullPrice = (5 / 100) * clothesPrice
  discount = clothesPrice - fullPrice
  print(f"The price with discount is: R${discount:.2f}")
else:
  print(f"Price without discount: R${clothesPrice:.2f}")