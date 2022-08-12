# LINGUAGEM: Python 3.9 (Python 3.9.4)

# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
# mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

from math import sqrt

a, b, c = map (float, input().split(' '))

# calculo do delta
delta = b**2 - 4 * a * c

if delta < 0 or a == 0:
    print('Impossivel calcular')
elif delta == 0:
    x = ( -b + sqrt(delta) ) / (2*a)
    print(f'R1 = {x:.5f}')
    print(f'R2 = {x:.5f}')
else:
    x1 = ( -b + sqrt(delta) )/ (2*a)
    x2 = ( -b - sqrt(delta) ) / (2*a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
