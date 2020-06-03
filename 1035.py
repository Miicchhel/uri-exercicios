'''
URI Online Judge | 1035
autor: Michel Melo
'''

A, B, C, D = input().split(' ')

'''
def teste_selecao(A,B,C,D):
    if A%2==1:
        return 'Valores nao aceitos'
    if (C or D) < 0:
        return 'Valores nao aceitos'
    if B < C:
        return 'Valores nao aceitos'
    if D < A:
        return 'Valores nao aceitos'
    if C+D < A+B:
        return 'Valores nao aceitos'
    return 'Valores aceitos'
'''
'''
def teste_selecao(A,B,C,D):
    if (A%2==1 ) or ((C or D) < 0) or (B < C ) or (D < A) or (C+D < A+B):
        return 'Valores nao aceitos'
    return 'Valores aceitos'
'''

def teste_selecao(A,B,C,D):
    if ((B > C) and (D > A)) and ((C+D > A+B) and (C>=0 and D>=0)) and (A%2==0):
        return 'Valores aceitos'
    return 'Valores nao aceitos'

print(teste_selecao(int(A),int(B),int(C),int(D)))
