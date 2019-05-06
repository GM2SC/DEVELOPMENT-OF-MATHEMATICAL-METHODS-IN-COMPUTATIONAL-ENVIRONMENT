# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:13:11 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@author: 
        Prof. Dr. Denis C. L. Costa
        Prof. Ms. Maurício Maia Ribeiro
        
        Discentes:
            Heictor Alves de Oliveira Costa
            Diego Yukio Nakashima
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Análise de Interpolação Cúbica II
        
Nome do sript: calculo_z

Disponível em:


"""
# Bibliotecas Utilizadas
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
z = [0.000, 0.025, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400,\
     0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.800, 0.850, 0.900,\
     0.950, 1.000, 1.100, 1.200, 1.300, 1.400, 1.500, 1.600, 1.700, 1.800,\
     1.900, 2.000, 2.200, 2.400, 2.600, 2.800]
print ('Posições da Concentração (mm) =', z)
print('')
print ('===================================================================')
erfz =[0.0000, 0.0282, 0.0564, 0.1125, 0.1680, 0.2227, 0.2763, 0.3286, 0.3794,\
       0.4284, 0.4755, 0.5202, 0.5633, 0.6039, 0.6420, 0.6778, 0.7112, 0.7421,\
       0.7707, 0.7970, 0.8209, 0.8427, 0.8802, 0.9103, 0.9340, 0.9523, 0.9661,\
       0.9763, 0.9838, 0.9891, 0.9928, 0.9953, 0.9981, 0.9993, 0.9998, 0.9999]
print ('Valores de erfz =',erfz)
print('')
print ('===================================================================')
f = interp1d(z, erfz)
erfz1 = interp1d(z, erfz, kind='cubic',fill_value="extrapolate")

z1 = np.linspace(0, 2.8, num=15)

z_interpol=input('Entre com o valor de z_interpol --> ')
ERF_INTERPOL=abs(erfz1(z_interpol));
print('O valor INTERPOLADO de erf é  >>>',ERF_INTERPOL)

plt.plot(z, erfz, 'oy', z1, f(z1), '--k', z1, erfz1(z1), '*r')
plt.title(' ERF em função de Z ')
plt.xlabel(' Valores de z ')
plt.ylabel ( 'Valores de erf(z)')
plt.title(' Erro de Gauss em Função de Z ')
plt.legend(["Dados Reais","Projeção dos Dados","Dados Interpolados"],loc=4)
plt.grid (True)
plt.show()

print('===================================')
print('Fim do programa calaculo_z')
print('===================================')

