# Escreva um programa que leia o nome do patrono.
# 1. Se o patrono for cervo, exiba a mensagem: “Cervo é o patrono do Harry Potter”.
# 2. Caso contrário, exiba a mensagem “<entrada> não é patrono do Harry Potter”,
# substituindo a expressão <entrada> pela string fornecida como entrada

patronum = input("Type Harry Potter Patronus (Digite o Patronus do Harry Potter):  ").lower()
if patronum == "cervo":
  print(f"{patronum} é o patrono do Harry Potter")
else:
  print(f"{patronum} não é patrono do Harry Potter")
  