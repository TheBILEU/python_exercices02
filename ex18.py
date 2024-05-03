# 3.a. Dia da semana
# Escreva um programa que leia um número inteiro, correspondente ao dia de hoje na semana.
# Por exemplo, domingo é 0, segunda é 1, terça é 2, …, sábado é 6.
# Se o usuário digitar um número inteiro diferente destes, imprima:
# “A entrada X é inválida”, onde X é o valor fornecido.
# Após isso, peça que o usuário também digite um número de dias no futuro a partir de hoje.
# Como saída, determine qual é o dia da semana após essa quantidade de dias, com a seguinte
# mensagem:
# “Hoje é X e o dia futuro é Y”

day = int(input("Digite um número que corresponda ao dia de hoja na semana: "))
futureDay = int(input("Digite um número de dias no futuro a partir de hoje: "))
soma = day + futureDay
dateDay = ''
dateSoma = ''

if (day < 0 or day > 6):
  print(f"A entrada {day} é inválida")
else:
  if (day == 0):
    dateDay = 'domingo'
  elif (day == 1):
    dateDay = 'segunda-feira'
  elif (day == 2):
    dateDay = 'terça-feira'
  elif (day == 3):
    dateDay = 'quarta-feira'
  elif (day == 4):
    dateDay = 'quinta-feira'
  elif (day == 5):
    dateDay = 'sexta-feira'
  elif (day == 6):
    dateDay = 'sábado'

  if (soma == 0):
    dateSoma = 'domingo'
  elif (soma == 1):
    dateSoma = 'segunda-feira'
  elif (soma == 2):
    dateSoma = 'terça-feira'
  elif (soma == 3):
    dateSoma = 'quarta-feira'
  elif (soma == 4):
    dateSoma = 'quinta-feira'
  elif (soma == 5):
    dateSoma = 'sexta-feira'
  elif (soma == 6):
    dateSoma = 'sábado'

  semana = soma//7
  
  if (soma < 6):
    print (f"Hoje é {dateDay} e o dia futuro é {dateSoma}")
  elif (soma > 6):
    soma = soma - 7*semana
    if (soma == 0):
      dateSoma = 'domingo'
    elif (soma == 1):
      dateSoma = 'segunda-feira'
    elif (soma == 2):
      dateSoma = 'terça-feira'
    elif (soma == 3):
      dateSoma = 'quarta-feira'
    elif (soma == 4):
      dateSoma = 'quinta-feira'
    elif (soma == 5):
      dateSoma = 'sexta-feira'
    elif (soma == 6):
      dateSoma = 'sábado'
      
    print (f"Hoje é {dateDay} e o dia futuro é {dateSoma}")