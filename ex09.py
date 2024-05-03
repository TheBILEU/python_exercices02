# Escreva um programa que leia 3 números inteiros distintos. Como saída, imprima o número do
# meio, isto é, o número cujo valor está entre o maior e o menor número.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if (num2 < num3 and num2 > num1) or (num2 < num1 and num2 > num3):
  print(num2)
elif (num1 < num3 and num1 > num2) or (num1 < num2 and num1 > num3): 
  print(num1)
else:
  print(num3)