# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:30:45 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@author: 
        Prof. Dr. Denis C. L. Costa
        
        Discentes:
            Heictor Alves de Oliveira Costa
            Lucas Pompeu Neves
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Função Polinomial do 3º grau em Python

Nome do sript: funcao3

Disponível em: 

"""

# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função do 3º grau : f3 = ax³ + bx² + cx + d
print('Coeficientes da Função do 3º grau')
# Coeficientes: a (a ≠ 0), b, c e d
a = -3
b = 9
c = -5
d = 6

print('Coeficiente: a =', a)
print('Coeficiente: b =', b)
print('Coeficiente: c =', c)
print('Coeficiente: d =', d)

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(-10,10,20)
f3 = a*x**3 + b*x**2 + c*x + d

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de f3
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,f3,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função do 3º grau')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao3 ===')
print('')
input("Acione <Ctrl + l> para limpar o console")

