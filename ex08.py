number = int(input('Digite um número de três digitos: '))

# 123 // 100 = 1
# 123 % 100 = 23

last_numbers = number % 100 

# print(number)
# print(last_numbers)

if number % last_numbers == 0:
  print("SIM")
else:
 print("NÃO")