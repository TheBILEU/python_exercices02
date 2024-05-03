# Escreva um programa para calcular a área de um triângulo, a partir das medidas dos três lados,
# fornecidas pelo usuário, em qualquer ordem. O algoritmo não pode permitir a entrada de dados
# inválidos, ou seja, medidas menores ou iguais a zero, ou medidas que não correspondam às de
# um triângulo.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if (a <= 0) and (b <= 0) and (c <= 0) and ((a < b + c) and (b < a + c) and (c < a + b)):
  print('Inválido')
else:
  p = (a + b + c) / 2
  aHeron = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
  print('Está é a área do triângulo: ', round(aHeron, 1))