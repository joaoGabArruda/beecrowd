# Linguagem: Python 3.9 (Python 3.9.4)

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
# calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula.

import math

lista = input()
x1,y1 = lista.split(' ')
x1 = float(x1)
y1 = float(y1)

lista = input()
x2,y2 = lista.split(' ')
x2 = float(x2)
y2 = float(y2)

distancia = (x2 - x1)**2 + (y2 - y1)**2
distancia = math.sqrt(distancia)

print(f'{distancia:.4f}')
