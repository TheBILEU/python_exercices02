# Escreva um programa que leia dois números inteiros.
# Se o produto dos dois números for par, imprima a soma deles.
# Caso contrário, ou seja, se for ímpar, imprima a diferença do segundo pelo primeiro número.

number = int(input("Type the first number: "))
number2 = int(input("Type the second: "))
numberResult = number * number2

if numberResult % 2 == 0:
  print("This number is even (Esse número é par)")
  sum = number + number2
  print(f"The sum is: {sum} (Soma)")
else:
  print("This number is odd (Esse número é ímpar)")
  sub = number2 - number
  print(f"The sub is: {sub} (Subtração)")