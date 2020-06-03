''' 
URI Online Judge | 1020
autor: Michel Melo
'''

entrada = int(input())

anos = entrada//365
entrada = entrada - anos * 365

meses = entrada//30
entrada = entrada - meses*30

dias=entrada

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos, meses, dias))
