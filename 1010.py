'''
URI Online Judge | 1010
autor: Michel Melo
'''

id_peca1, num_peca1, valor_peca1 = input().split(' ')
id_peca2, num_peca2, valor_peca2 = input().split(' ')

total = int(num_peca1)*float(valor_peca1) + int(num_peca2)*float(valor_peca2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
