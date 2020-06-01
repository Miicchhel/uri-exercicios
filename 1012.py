'''
URI Online Judge | 1012
autor: Michel Melo
'''

A, B, C = input().split(' ')

triangulo = (float(A) * float(C)) / 2
circulo = 3.14159 * float(C)**2
trapezio = (float(A) + float(B)) * float(C) / 2
quadrado = float(B)**2
retangulo = float(A) * float(B)

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
