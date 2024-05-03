# Escreva um programa que leia um valor inteiro 𝑚 tal que 1 ≤ 𝑚 ≤ 12. Como saída, imprima
# por extenso o nome do mês correspondente no ano. Se a entrada não corresponder a nenhum
# dos meses do ano, imprima: “número de mês inválido”.

month = int(input("Digite o número do mês desejado: "))

if (month <= 0) or (month > 12):
  print("Mês inválido")
else:
  if(month == 1):
    print("Janeiro")
  
  elif(month == 2):
    print("Fevereiro")
  
  elif(month == 3):
    print("Março")
  
  elif(month == 4):
    print("Abril")
  
  elif(month == 5):
    print("Maio")
  
  elif(month == 6):
    print("Junho")
    
  elif(month == 7):
    print("Julho")
    
  elif(month == 8):
    print("Agosto")
    
  elif(month == 9):
    print("Setembro")
    
  elif(month == 10):
    print("Outubro")
    
  elif(month == 11):
    print("Novembro")
    
  elif(month == 12):
    print("Dezembro")
  
 
  