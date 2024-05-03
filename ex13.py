# Considere dois números reais 𝑎 e 𝑏, sendo 𝑏 > 𝑎. Um número real 𝑥 pertence ao intervalo
# [𝑎, 𝑏] se 𝑎 ≤ 𝑥 ≤ 𝑏.
# Escreva um programa que leia os números reais 𝑥, 𝑎, 𝑏, nesta ordem
# Se 𝑥 pertencer ao intervalo, imprima a seguinte mensagem:
# “x pertence ao intervalo [a, b]”
# Caso contrário, imprima a seguinte mensagem:
# “x não pertence ao intervalo [a, b]”
# Se as entradas forem inválidas, ou seja, se 𝑏 ≤ 𝑎, imprima a seguinte mensagem:
# “entradas a e b inválidas”


a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
x = float(input('Digite o terceiro valor: '))

if (b < a) or (b == a):
  print('Entrada a e b inválidos')
else:
  if (x < b) and (x > a):
    print(f"{x} pertence ao intervalo entre [{a} e {b}]")
  else:
    print(f"{x} não pertence ao intervalo entre [{a} e {b}]")