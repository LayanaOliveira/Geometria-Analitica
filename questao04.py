#ALTERNATIVA A 
#A reta r é secante a circunferência C
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

#Verifica a posição em relação a circunferência
if raio < distancia:
    pos = 'Externa'
elif raio > distancia:
    pos = 'Secante'
else:
    pos = 'Tangente'

print('''A posição entre a reta s e a circunferência ʎ é {}'''.format(pos))

#ALTERNATIVA A 
# Eles tem pelo menos um ponto em comum

if raio < distancia:
    pos = 'não possuem pontos em comum.'
elif raio > distancia:
    pos = 'possuem pelo menos dois pontos em comum '
else:
    pos = 'eles tem pelo menos um ponto em comum'
    
print('A posição entre a reta s e a circunferência ʎ indica que {}'.format(pos))

# ALTERNATIVA D e E
#Utizize esse código para verificar se um par ordenado pertence a reta r
l, w = input('Informe um par de coordenadas para verificar se pertence a reta na forma(x,y): ').split(',')
l, w = float(l), float(w)

if l + b*w + c == 0:
    print('O par ordenado pertence a reta r')
else:
    print('O par ordenado não pertence a reta r')

# ALTERNATIVA D e E
#Utilize esse códico para verificar se um par ordenado pertence a reta C

print('''É necessário que seu par ordenado seja números decimais (float), se for necessário utilize o bloco seguinte 
para realizar cálculos''')
g, h = input('Informe um par de coordenadas para verificar se pertence a circunferência na forma(x,y): ').split(',')
g, h = float(g), float(h)

if g**2 + h**2 + xc*g + yc*h + f == 0:
    print('O par ordenado pertence a circunferência C')
else:
    print('O par ordenado não pertence a circunferência C')
    
tipo = int(input('''Informe o tipo de cálculo de acordo com o número da tabela:
1 - divisão
2 - radiciação
'''))

if tipo == 1:
    a, b = input('Digite separado por vírgula os números que você deseja dividir, exemplo (a,b)').split(",")
    a, b = int(a), int(b)

    solucao = a/b
    solucaoformat = "{:.2f}".format(round(solucao, 2))

    print('O resultado da divisão {}/{} é {}'.format(a, b, solucaoformat))
    
if tipo == 2:
    rad = float(input('Informe o número que você deseja extrair a raiz: '))
    solucao = math.sqrt(rad)
    
    solucaoformat = "{:.2f}".format(round(solucao, 2))

    print('O resultado é {}'.format(solucaoformat))
    
else:
    print('DIGITE UMA OPÇÃO VÁLIDA')