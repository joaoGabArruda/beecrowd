# Linguagem: Python 3.9 (Python 3.9.4)

# 

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
