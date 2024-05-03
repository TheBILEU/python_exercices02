# 4.b. Consumo de combustível
  # Escreva um programa que leia, nesta ordem:
  # o percurso de uma viagem (em quilômetros)
  # o tipo do carro (A ou B)
  # Sabe-se que um carro tipo A faz 8 km com um litro de gasolina e um tipo B faz 12 km/l.
  # Como saída, informe o consumo estimado de combustível

route = float(input("Route of a trip(km): "))
carType = input("A or B: ")

if carType == 'A': 
  consu = route // 8
  print(f"{consu}L")
elif carType == 'B':
  consu = route // 12
  print(f"{consu}L")

# 8km - 1 L
# route km - consu L

# route * 1 = 8 * consu
# consu = route / 8