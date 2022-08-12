# NÃO CONSEGUI RESOLVER!!!

# versão 1: Wrong answer (5%)

import math

valor = float(input())
N, x = math.modf(valor)

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while x != 0:
    if x - 100 >= 0:
        x -= 100
        cem += 1
    elif x - 50 >= 0:
        x -= 50
        cinquenta += 1
    elif x - 20 >= 0:
        x -= 20
        vinte += 1
    elif x - 10 >= 0:
        x -= 10
        dez += 1
    elif x - 5 >= 0:
        x -= 5
        cinco += 1
    elif x - 2 >= 0:
        x -= 2
        dois += 1
    else:
        x -= 1
        um += 1

cinquenta_cents = 0
vintecinco_cents = 0
dez_cents = 0
cinco_cents = 0
um_cent = 0

N = round(N,2)

while N != 0.00:
    if N - 0.50 >= 0.00:
        N -= 0.50
        N = round(N,2)
        cinquenta_cents += 1
    elif N - 0.25 >= 0.00:
        N -= 0.25
        N = round(N,2)
        vintecinco_cents += 1
    elif N - 0.10 >= 0.00:
        N -= 0.1
        N = round(N,2)
        dez_cents += 1
    elif N - 0.05 >= 0.00:
        N -= 0.05
        N = round(N,2)
        cinco_cents += 1
    else:
        N -= 0.01
        N = round(N,2)
        um_cent += 1


print('NOTAS:')
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')

print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1,00')
print(f'{cinquenta_cents} moeda(s) de R$ 0.50')
print(f'{vintecinco_cents} moeda(s) de R$ 0.25')
print(f'{dez_cents} moeda(s) de R$ 0.10')
print(f'{cinco_cents} moeda(s) de R$ 0.05')
print(f'{um_cent} moeda(s) de R$ 0.01')



# versão 2: Wrong answer (10%)

from decimal import *

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidade_notas = int(valor/nota)
    print(f'{quantidade_notas} nota(s) de R$ {nota:.2f}')
    valor -= quantidade_notas * nota

print('MOEDAS:')
getcontext().prec = 2
valor = Decimal(valor)

for moeda in moedas:
    moeda = Decimal (moeda)
    quantidade_moedas = int(valor/moeda)
    print(f'{quantidade_moedas} nota(s) de R$ {moeda:.2f}')
    valor -= quantidade_moedas * moeda
    
    

# versão 3: Time limit exceeded

import math
from decimal import *

valor = float(input())
N, x = math.modf(valor)

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while x != 0:
    if x - 100 >= 0:
        x -= 100
        cem += 1
    elif x - 50 >= 0:
        x -= 50
        cinquenta += 1
    elif x - 20 >= 0:
        x -= 20
        vinte += 1
    elif x - 10 >= 0:
        x -= 10
        dez += 1
    elif x - 5 >= 0:
        x -= 5
        cinco += 1
    elif x - 2 >= 0:
        x -= 2
        dois += 1
    else:
        x -= 1
        um += 1


cinquenta_cents = 0
vintecinco_cents = 0
dez_cents = 0
cinco_cents = 0
um_cent = 0

getcontext().prec = 2
N = Decimal(N)

while N != Decimal ('0.00'):
    if N - Decimal('0.50') >= 0.00:
        N -= Decimal('0.50')
        cinquenta_cents += 1
    elif N - Decimal('0.25') >= 0.00:
        N -= Decimal('0.25')
        vintecinco_cents += 1
    elif N - Decimal('0.10') >= 0.00:
        N -= Decimal ('0.1')
        dez_cents += 1
    elif N - Decimal('0.05') >= 0.00:
        N -= Decimal ('0.05')
        cinco_cents += 1
    else:
        N -= Decimal ('0.01')
        um_cent += 1


print('NOTAS:')
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')

print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1,00')
print(f'{cinquenta_cents} moeda(s) de R$ 0.50')
print(f'{vintecinco_cents} moeda(s) de R$ 0.25')
print(f'{dez_cents} moeda(s) de R$ 0.10')
print(f'{cinco_cents} moeda(s) de R$ 0.05')
print(f'{um_cent} moeda(s) de R$ 0.01')
