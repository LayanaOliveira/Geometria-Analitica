# Descreva a posição da reta s em relação à circunferência ʎ, em cada um dos casos  a seguir: 
#Utlilize esse código para equações de circunferência em sua forma reduzida
import math
reta = input("Digite a equação da reta no formato Ax + By + C: ")
x, y = input("Digite o centro da circunferência ʎ, no formato (x,y): ").split(",")
raio = int(input("Digite o valor do raio: "))

x, y = float(x), float(y)

# Separa os coeficientes A, B e C da equação da reta
A = float(eq_reta.split('x')[0].replace(' ', '').replace('A', ''))
B = float(eq_reta.split('x')[1].split('y')[0].replace(' ', '').replace('B', ''))
C = float(eq_reta.split('y')[1].replace(' ', '').replace('=', '').replace('C', ''))

# Calcula a distância entre o ponto e a reta
distancia = abs(A*x + B*y + C) / math.sqrt(A**2 + B**2)
dtcFormatada = "{:.2f}".format(round(distancia, 2))

#Verifica a posição em relação a circunferência
if raio < distancia:
    pos = 'Externa'
elif raio > distancia:
    pos = 'Secante'
else:
    pos = 'Tangente'

print('''A distância entre a reta s e a circunferência ʎ é igual a {}.
Sua posição é {}'''.format(dtcFormatada, pos))

# Descreva a posição da reta s em relação à circunferência ʎ, em cada um dos casos  a seguir: 
#Utlilize esse código para equações de circunferência em sua forma geral
import math

a = float(input("Digite o valor de a da reta s: "))
b = float(input("Digite o valor de b da reta s: "))
c = float(input("Digite o valor de c da reta s: "))

xc, yc = input('Infome os valores que acompanham x e y da equação da circunferência, respectivamente. exemplo(x,y)').split(',')
xc, yc = float(xc), float(yc)

xcc = xc/-2
ycc = yc/-2

f = float(input('Por fim, informe o termo independente da equação geral da circunferência: '))

raio = math.sqrt(xcc**2 + ycc**2 - f)

distancia = abs(a*xcc + b*ycc + c) / math.sqrt(a**2 + a**2)
dtcFormatada = "{:.2f}".format(round(distancia, 2))

#Verifica a posição em relação a circunferência
if raio < distancia:
    pos = 'Externa'
elif raio > distancia:
    pos = 'Secante'
else:
    pos = 'Tangente'

print('''A distância entre a reta s e a circunferência ʎ é igual a {}.
Sua posição é {}'''.format(dtcFormatada, pos))