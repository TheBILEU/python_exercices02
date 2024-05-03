# Escreva um programa que converta uma temperatura da escala Celsius para Fahrenheit ou vice-versa. 
# Para isso, você deverá ler duas entradas:
# 1. escala em que a temperatura está representada: C para Celsius, ou F para Fahrenheit.
# 2. valor da temperatura.
# Como saída, imprima:
# a temperatura convertida para a outra escala, arredondada em uma casa decimal

value = int(input("Temperature value: "))  
temperature = input("What temperature scale did you enter represent to convert(C for Celsius or F for Fahrenheit): ")

if temperature == "F":
  c = 5 / 9 * (value - 32)
  print(f"{c:.1f} C°")
elif temperature == "C":
  f = (value * 1.8) + 32
  print(f"{f:.1f} F°")