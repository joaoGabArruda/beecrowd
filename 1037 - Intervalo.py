# LINGUAGEM: Python 3.9 (Python 3.9.4

# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos 
# ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, 
# deverá ser impressa a mensagem “Fora de intervalo”.
# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

x = float(input())

if x >= 0.0 and x <= 25.0:
    print('Intervalo [0,25]')
elif x > 25.0 and x <= 50.0:
    print('Intervalo (25,50]')
elif x > 50.0 and x <= 75.0:
    print('Intervalo (50,75]')
elif x > 75.0 and x <= 100.0:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
