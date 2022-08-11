# Linguagem: Python 3.9 (Python 3.9.4)

# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos 
# casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

N = int(input())
anos = 0
meses = 0
dias = 0

while N != 0:
    if N >= 365:
        N -= 365
        anos += 1
    elif N >= 30 :
        N -= 30
        meses += 1
    else:
        dias = N
        N = 0

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
