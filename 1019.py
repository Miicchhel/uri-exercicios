''' 
URI Online Judge | 1019
autor: Michel Melo
'''

entrada = int(input())

horas = entrada//60**2
entrada = entrada - horas * 60**2

minutos = entrada//60
entrada = entrada - minutos*60

segundos=entrada

print('{}:{}:{}'.format(horas, minutos, segundos))
