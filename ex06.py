# Faça um programa que leia as seguintes informações de uma pessoa, nesta ordem:
# Altura (em metros)
# Sexo (M ou F)
# Como saída, determine o peso ideal, arredondado com até duas casas decimais, dado por:
# Para homens: (72. 7 × 𝑎𝑙𝑡𝑢𝑟𝑎) − 58
# Para mulheres: (62. 1 × 𝑎𝑙𝑡𝑢𝑟𝑎) − 44. 7

height = float(input("Type a height: "))
gender = input("M or F: ")

if gender == 'M':
  weightM = (72.7 * height) - 58
  print(f"{weightM:.2f}KG")
elif gender == 'F':
  weightF = (62.1 * height) - 44.7
  print(f"{weightF:.2f}KG")