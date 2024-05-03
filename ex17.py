# Uma empresa decidiu dar uma gratificação diferenciada ao melhor funcionário do ano. A
# gratificação é determinada com base no número de horas extras trabalhadas e no número de
# horas não trabalhadas (horas que funcionário faltou ao serviço), conforme a tabela a seguir e o
# índice H determinado da seguinte forma:

# 𝐻 = (𝑛ú𝑚𝑒𝑟𝑜 𝑑𝑒 ℎ𝑜𝑟𝑎𝑠 𝑒𝑥𝑡𝑟𝑎) − 1 / 4 × (𝑛ú𝑚𝑒𝑟𝑜 𝑑𝑒 ℎ𝑜𝑟𝑎𝑠 𝑛ã𝑜 𝑡𝑟𝑎𝑏𝑎𝑙ℎ𝑎𝑑𝑎𝑠)

# Escreva um programa que leia:
# 1. O número de horas extras;
# 2. O número de horas que o funcionário faltou.

# Como saída, imprima a seguinte mensagem:
# “E extras e F de falta”
# “R$ G”
# Onde, E é o valor das horas extras, F é o valor das horas de faltas e G é o valor da gratificação

extraHour = float(input("O número de horas extras: "))
missHour = float(input("O número de horas que o funcionário faltou: "))

h = extraHour - ((1 / 4) * missHour)

if (h > 400):
  print('Parabéns... funcionário do mês')
  print(f"Trabalhou por {extraHour} horas extras e teve {missHour} horas faltas")
  print("Sua gratificação será de R$500 reais")
elif (h <= 400):
  print('Parabéns pelo trabalho árduo')
  print(f"Trabalhou por {extraHour} horas extras e teve {missHour} horas faltas")
  print("Sua gratificação será de R$100 reais")