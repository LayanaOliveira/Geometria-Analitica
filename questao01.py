# ALTERNATIVA A - Construa o gráfico cartesiano representando o trecho da auto estrada e o ponto P.

import matplotlib.pyplot as plt
import numpy as np
import math

# Receber os valores da equação geral da reta
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

x1 = float(input('Valor que deseja atribuir a x: '))
y1 = (-a*x1 - c)/b

x2 = float(input('Outro valor que deseja atribuir a x: '))
y2 = (-a*x2 - c)/b

print(y1, y2)

plt.plot([x1, x2], [y1, y2])

plt.xlim(0, 8)
plt.ylim(0, 8)

plt.grid(True)

plt.show()


#ALTERNATIVA B 
# Sabendo que a estrada vicinal pode ser construída em qualquer posição, calcule o menos comprimeto possível dessa estrada

x_ponto = float(input("Digite a coordenada x do ponto: "))
y_ponto = float(input("Digite a coordenada y do ponto: "))
ponto = (x_ponto, y_ponto)

distancia = abs(a*x_ponto + b*y_ponto + c)/math.sqrt(a**2 + b**2)

dtcFormatada = "{:.2f}".format(round(distancia, 2))

print('O menor comprimento possível é {} km'.format(dtcFormatada))


# ALTERNATIVA C
# Determine as coordenadas do ponto Q da auto estrada de modo que a estrada vicinal tenha o menor comprimento possível
#Calculadora de equações do segundo grau

import math

# Define os coeficientes da equação ax^2 + bx + c = 0
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c
# Verifica se a equação tem raízes reais
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    # Caso delta seja igual a zero, há apenas uma raiz real
    x = -b / (2*a)
    print(f"A equação possui apenas uma raiz real: x = {x}")
else:
    # Caso delta seja maior que zero, há duas raízes reais
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")