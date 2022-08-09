# Linguagem: Python 3.9 (Python 3.9.4)

# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

lista = input()
A,B,C = lista.split(" ")

A = float(A)
B = float(B)
C = float(C)

print(f'TRIANGULO: {A*C/2:.3f}')
print(f'CIRCULO: {3.14159*C**2:.3f}')
print(f'TRAPEZIO: {(A+B)*C/2:.3f}')
print(f'QUADRADO: {B*B:.3f}')
print(f'RETANGULO: {A*B:.3f}')
