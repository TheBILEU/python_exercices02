a = float(input('Digite o valor correspondente a [a]: '))
b = float(input('Digite o valor correspondente a [b]: '))
xAB = float(input('Digite o valor que deseja de intervalo corresponde a [a,b]: '))
c = float(input('Digite o valor correspondente a [c]: '))
d = float(input('Digite o valor correspondente a [d]: '))
xCD = float(input('Digite o valor que deseja de intervalo corresponde a [c,d]: '))

if (b < a) or (b == a) and (d < c) or (d == c):
  print('Entradas inválidas')
else:
  if (xAB < b) and (xAB > a) and (xCD < d) and (xCD > c) :
    print(f"{xAB} pertence ao intervalo entre [{a} e {b}]")
    print(f"{xCD} pertence ao intervalo entre [{c} e {d}]")
    if (xAB == xCD):
      print('Há intersecção')
    else:
      print('Não há intersecção')
  else:
    print(f"{xAB} não pertence ao intervalo entre [{a} e {b}]")
    print(f"{xCD} não pertence ao intervalo entre [{c} e {d}]")
    


    
    