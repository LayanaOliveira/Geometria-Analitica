# Distância entre as retas paralelas
import math
print('Digite os termos da equação, em caso de inexistência, insira o valor 0')

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
cr = float(input("Digite o valor de c da reta r: "))
cs = float(input("Digite o valor de c da reta s: "))

distancia = abs(cr - cs)/math.sqrt(a**2 + b**2)

distanciaFormatada = "{:.2f}".format(round(distancia, 2))

print('''A distância entre as retas paralelas
é: {}'''.format(distanciaFormatada))
