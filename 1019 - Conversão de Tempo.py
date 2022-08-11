# Linguagem: Python 3.9 (Python 3.9.4)

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado 
# evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.


N = int(input())
hora = 0
minuto = 0
segundo = 0

while N != 0:
    if N >= 3600:
        N -= 3600
        hora += 1
    elif N >= 60 :
        N -= 60
        minuto += 1
    else:
        segundo = N
        N = 0

print(hora,minuto,segundo,sep=':')
