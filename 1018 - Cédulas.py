# Linguagem: Python 3.9 (Python 3.9.4)

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual 
# o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir 
# mostre o valor lido e a relação de notas necessárias.


N = int(input())
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

print(N)

while N != 0:
    if N - 100 >= 0:
        N = N - 100
        cem += 1
    elif N - 50 >= 0:
        N = N - 50
        cinquenta += 1
    elif N - 20 >= 0:
        N = N - 20
        vinte += 1
    elif N - 10 >= 0:
        N = N - 10
        dez += 1
    elif N - 5 >= 0:
        N = N - 5
        cinco += 1
    elif N - 2 >= 0:
        N = N - 2
        dois += 1
    else:
        N = N - 1
        um += 1

print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
