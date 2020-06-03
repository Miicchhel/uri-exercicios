'''
URI Online Judge | 1013
autor: Michel Melo
'''

A, B, C = input().split(' ')

maiorAB = (int(A) + int(B) + abs(int(A) - int(B))) / 2

maiorABC = (maiorAB + int(C) + abs(maiorAB - int(C))) / 2

print("{} eh o maior".format(int(maiorABC)))
