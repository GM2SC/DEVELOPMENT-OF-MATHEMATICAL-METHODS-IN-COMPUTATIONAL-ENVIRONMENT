# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:20:48 2019

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
        Análise de Interpolação Cúbica I
        
Nome do sript: calculo_erf

Disponível em:

"""

# Bibliotecas Utilizadas
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
erfz = np.array([0.0000, 0.0282, 0.0564, 0.1125, 0.1680, 0.2227, 0.2763, 0.3286,\
                 0.3794, 0.4284, 0.4755, 0.5202, 0.5633, 0.6039, 0.6420, 0.6778,\
                 0.7112, 0.7421, 0.7707, 0.7970, 0.8209, 0.8427, 0.8802, 0.9103,\
                 0.9340, 0.9523, 0.9661, 0.9763, 0.9838, 0.9891, 0.9928, 0.9953,\
                 0.9981, 0.9993, 0.9998, 0.9999])
print ('Função Erro de Gauss =', erfz)
print('')
print ('===================================================================')
z = np.array([0.000, 0.025, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350,\
              0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.800,\
              0.850, 0.900, 0.950, 1.000, 1.100, 1.200, 1.300, 1.400, 1.500,\
              1.600, 1.700, 1.800, 1.900, 2.000, 2.200, 2.400, 2.600, 2.800])
print ('Posições da Concentração (mm) =',z)

f = interp1d(erfz, z)
z1 = interp1d(erfz, z, kind='cubic',fill_value="extrapolate")

erfz1 = np.arange(0.0000, 0.9999, 0.0999)

erfz_interpol=input('Entre com o valor de erfz_interpol --> ');

Z_INTERPOL=abs(z1(erfz_interpol));
print('O valor INTERPOLADO de z é >>>',Z_INTERPOL)


plt.plot(erfz, z, 'oy', erfz1, f(erfz1), '--b', erfz1, z1(erfz1), '>r')
plt.title('Z em Função do Erro de Gauss')
plt.xlabel(' Valores de Erf ');
plt.ylabel ( 'Valores de Z');
plt.legend(["Dados Reais","Projeção dos Dados","Dados Interpolados"],loc=2)
plt.grid(True)
plt.show()

print('===================================')
print('Fim do programa calaculo_erf')
print('===================================')

