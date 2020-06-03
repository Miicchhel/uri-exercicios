'''
URI Online Judge | 1015
autor: Michel Melo
'''

x1, y1 = input().split(' ')
x2, y2 = input().split(' ')

distancia = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2 ) ** (1/2)

print('{:.4f}'.format(distancia))
