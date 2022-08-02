# Linguagem: Python 3.9 (Python 3.9.4)
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
# Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

raio = float(input()) #recebe o input do teclado, converte em float e insere na vaiável raio
n = 3.14159 # define n como sendo esse valor
area = n * raio**2 # faz o cálculo da area
print(f'A={area:.4f}') # faz o print ajustando o numero de casas decimais através de "f-strings"
