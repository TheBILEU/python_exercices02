# Escreva um programa que leia 02 valores, x e y, que representam as coordenadas de um
# ponto no plano cartesiano.
# Como saída, determine em que quadrante (Q1, Q2, Q3 ou Q4) o ponto está situado, ou se ele
# está sobre um dos eixos cartesianos (Eixo X, Eixo Y), ou se ele está na origem 𝑥 = 𝑦 = 0
# (Origem).

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if (x > 0) and (y > 0):
  print('O ponto estará no primeiro quadrante (Q1)')
elif (x < 0) and (y > 0):
  print('O ponto estará no segundo quadrante (Q2)')
elif (x < 0) and (y < 0):
  print('O ponto estará no terceiro quadrante (Q3)')
elif (x > 0) and (y < 0):
  print('O ponto estará no quarto quadrante (Q4)')
elif (x == 0) and (y < 0 or y > 0):
  print('O ponto estará sobre o Eixo Y')
elif (x < 0 or x > 0) and (y == 0):
  print('O ponto estará sobre o Eixo X')
elif (x == y == 0):
  print('O ponto estará na Origem')