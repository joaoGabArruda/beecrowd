# Linguagem: Python 3.9 (Python 3.9.4)

# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, 
# ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através 
# de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) 
# e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, 
# calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

# Formula da velocidade : V = S/T


tempo = int(input())
velocidade = int(input())

distancia = velocidade * tempo # Da fórmula, acha a distancia

print(f'{distancia/12:.3f}') # Divide por 12 p/ achar a quantidade de litros gasta
