# Linguagem: Python 3.9 (Python 3.9.4)

# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

codigo, quantidade = map(int, input().split(' '))

if codigo == 1 :
    print(f'Total: R$ {quantidade*4:.2f}')
elif codigo == 2 :
    print(f'Total: R$ {quantidade*4.5:.2f}')
elif codigo == 3 :
    print(f'Total: R$ {quantidade*5:.2f}')
elif codigo == 4 :
    print(f'Total: R$ {quantidade*2:.2f}')
elif codigo == 5 :
    print(f'Total: R$ {quantidade*1.50:.2f}')
