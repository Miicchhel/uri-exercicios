''' 
URI Online Judge | 1017
autor: Michel Melo
'''
media_carro = 12
tempo = int(input())
velocidade = int(input())

litros = (tempo * velocidade) / media_carro

print('{:.3f}'.format(litros))
