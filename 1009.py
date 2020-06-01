'''
URI Online Judge | 1009
autor: Michel Melo
'''

vendedor = input()
salario = float(input())
total_vendas = float(input())

bonus = total_vendas * 0.15

total = salario + bonus

print('TOTAL = R$ {:.2f}'.format(total))
