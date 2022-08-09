# Linguagem: Python 3.9 (Python 3.9.4)

# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

lista = input()
a,b,c = lista.split(" ")

a = int(a)
b = int(b)
c = int(c)

MaiorAB = ((a+b+abs(a-b))//2)

if MaiorAB > c:
    print(f'{MaiorAB} eh o maior')
else:
    print(f'{c} eh o maior')
