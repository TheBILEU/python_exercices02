# Faça um programa que informe o risco de problemas cardíacos de uma pessoa, a partir da
# leitura da idade e do índice de massa corporal (IMC), nessa ordem. 

age = int(input("How old are you? "))
imc = float(input("IMC: "))

if (age <= 0 or age > 100) and (imc <= 0):
  print("Invalid Data")
elif (age > 0 or age < 100) and (imc > 0): 
  print(f"{age} years / IMC: {imc:.1f}")
  if (age < 45) and (imc < 22):
    print("Risco: baixo")
  elif (age < 45) and (imc >= 22) or (age >= 45) and (imc < 22):
    print("Risco: médio")
  elif (age >= 45) and (imc >= 22):
    print("Risco: alto")