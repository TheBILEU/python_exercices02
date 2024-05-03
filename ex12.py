# Escreva um programa que determine o valor total a ser pago pela conta de energia elétrica,
# com base nas seguintes entradas:
# 1. O consumo de energia (em kWh); e
# 2. O tipo de instalação (R para residências, I para indústrias, e C para comércios).

# Como saída :
# 1. Valor total da conta de energia elétrica arredondado para duas casas decimais, caso
# os dados sejam válidos OU a mensagem "Dados inválidos" caso os dados sejam
# inválidos. Os dados são inválidos quando o consumo é negativo ou o tipo de
# instalação é diferente das letras R, I ou C.

power = float(input("Consumo de energia em (kWh): "))
plant = input("Tipo de instalação (R, C, I): ").lower()

if (plant != 'r') and (plant != 'c') and (plant != 'i') or (power <= 0):
  print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
  print("Dados inválidos")
else:
  if (plant == 'r') and (power <= 500):
    fullPrice = power * 0.44
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")
  elif (plant == 'r') and (power > 500):
    fullPrice = power * 0.65
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")
  elif (plant == 'c') and (power <= 1000):
    fullPrice = power * 0.55
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")
  elif (plant == 'c') and (power > 1000):
    fullPrice = power * 0.60
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")
  elif (plant == 'i') and (power <= 5000):
    fullPrice = power * 0.55
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")
  elif (plant == 'i') and (power > 5000):
    fullPrice = power * 0.60
    print(f"Energia: {power} kWh; Instalação: {plant.capitalize()}")
    print(f"O valor total da energia para ser pago será de: R${fullPrice:.2f}")