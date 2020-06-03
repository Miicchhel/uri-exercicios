'''
URI Online Judge | 1021
autor: Michel Melo
'''

def mostrar(valor):
     #implementa a parte das notas
    n_100 = valor // 100
    valor = valor - (n_100 *100)
    
    n_50 = valor // 50
    valor = valor - (n_50 *50)
    
    n_20 = valor // 20
    valor = valor - (n_20 *20)
    
    n_10 = valor // 10
    valor = valor - (n_10 *10)
    
    n_5 = valor // 5
    valor = valor - (n_5 *5)
    
    n_2 = valor // 2
    valor = valor - (n_2 *2)
    

    #implementa a parte das moedas
    n_1 = valor // 1
    valor = valor - (n_1 *1)
    
    n_05 = valor // 0.5
    valor = valor - (n_05 *0.5)
    
    n_025= valor // 0.25
    valor = valor - (n_025 *0.25)

    n_01 = valor // 0.1
    valor = valor - (n_01 *0.1)
    
    n_005 = valor // 0.05
    valor = valor - (n_005 *0.05)
    
    valor=valor*100
    
    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(int(n_100)))
    print('{} nota(s) de R$ 50.00'.format(int(n_50)))
    print('{} nota(s) de R$ 20.00'.format(int(n_20)))
    print('{} nota(s) de R$ 10.00'.format(int(n_10)))
    print('{} nota(s) de R$ 5.00'.format(int(n_5)))
    print('{} nota(s) de R$ 2.00'.format(int(n_2)))
    print('MOEDAS:') 
    print('{} moeda(s) de R$ 1.00'.format(int(n_1)))
    print('{} moeda(s) de R$ 0.50'.format(int(n_05)))
    print('{} moeda(s) de R$ 0.25'.format(int(n_025)))
    print('{} moeda(s) de R$ 0.10'.format(int(n_01)))
    print('{} moeda(s) de R$ 0.05'.format(int(n_005)))
    print('{} moeda(s) de R$ 0.01'.format(int(valor)))

valor = float(input())
if valor >= 0 and valor <= 1000000.00:
    mostrar(valor)
