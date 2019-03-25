# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:31:35 2019

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
        Representação de Gráfica de Funções com duas variáveis independentes
        
Nome do sript: graficos_3d

Disponível em:
    
"""
# Bibliotecas

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Comandos para plotar Gráficos em 3D
fig = plt.figure(1)
ax = Axes3D(fig)

# Valores de x:
x = np.arange(-5, 5, 0.25)
# Valores de y:
y = np.arange(-5, 5, 0.25)

# Função de duas Variáveis: z(x,y)
x, y = np.meshgrid(x, y)
z = x**2 + y**2
print('')

# Títulos do Gráfico 3D
ax.set_xlabel('Valores de x')
ax.set_ylabel('Valores de y')
ax.set_zlabel('Valores de z')
ax.set_title('Função z = f(x,y)')

# Layout do Gráfico 3D:
# Opções de cores: cmap --> escolha a letra correspondente
a =  'Spectral'
b =  'seismic'
c =  'coolwarm'
d =  'PRGn'
e = 'RdYlBu'
f = 'RdGy' 
g = 'RdYlGn'

ax.plot_surface(x, y, z, cmap = b)
print('')
print(' ==== Gráfico gerado pelo Programa integrais_triplas ====')

# Gráfico de Contornos
fig = plt.figure()
# n --> Número de linhas de contorno
n = 25
plt.contour(x, y, z, n)
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função z = f(x,y)')
plt.show()
