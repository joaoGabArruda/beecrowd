# Linguagem: Python 3.9 (Python 3.9.4)
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# OBSERVAÇÃO: Tive que fazer uma gambiarra de aceitar o input em uma única variável e depois separar em 3 pois estava dando runtime error ao tentar
# fazer um input por variável [EX: codigo1 = input(); numpecas1 = int(input()); valor1 = float(input()) ]. Caso o código abaixo falhe em algum momento,
# eles devem ter consertado o teste deles, então tente fazer igual o exemplo.

lista = input()
codigo1,numpecas1,valor1 = lista.split(" ")

numpecas1 = int(numpecas1)
valor1 = float(valor1)

lista = input()
codigo2,numpecas2,valor2 = lista.split(" ")

numpecas2 = int(numpecas2)
valor2 = float(valor2)

print(f'VALOR A PAGAR: R$ {numpecas1*valor1 + numpecas2*valor2:.2f}')
