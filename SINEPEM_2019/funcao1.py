# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:26:11 2019

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
        Funções Polinomiais de 1º e 2º graus em Python

Nome do sript: funcao1

Disponível em: 

"""
# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas 
import numpy as np

# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função do 1º grau : f1 = ax + b
print('Coeficientes da Função do 1º grau')
# Coeficiente Angular: a
a = 2
print('Coeficiente Angular: a =', a)

# Coeficiente Linear: b
b = 3
print('Coeficiente Linear: b =', b)

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(-2,2,20)
f1 = a*x + b

input("Pressione <enter> para representar graficamente")
print('')
# Representação Gráfica de f1
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,f1,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função do 1º grau')
plt.grid(True)
plt.show()







