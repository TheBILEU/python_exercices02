# 4.a. Tem troco?
  # Escreva um programa que leia dois números reais: preço e pagamento, nessa ordem.
  # Se o preço for maior que o pagamento, então o programa deve imprimir “Falta X”, onde
  # X é a diferença a ser paga.
  # Caso contrário, o programa deve imprimir “Troco de Y”, onde Y é o valor a ser
  # devolvido pelo comerciante ao comprador, que pode ser zero.

price = float(input("Price of the product: "))
paynment = float(input("Paynment value: "))

if price > paynment: 
  x = price - paynment
  print(f"R${x:.2f} left to pay")
elif paynment > price: 
  y = paynment - price
  print(f"R${y:.2f} in change")
