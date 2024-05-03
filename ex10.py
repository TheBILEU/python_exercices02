a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if ((a > 0) and (b > 0) and (c > 0)) and ((a < b + c) and (b < a + c) and (c < a + b)):
  if (a == b == c):
    print("Triângulo: equilátero")
  elif (a == b != c) or (a == c != b) or (b == c != a):
    print("Triângulo: isósceles")
  elif (a != b != c):
    print("Triângulo: escaleno")
else: 
  print("Inválido")  