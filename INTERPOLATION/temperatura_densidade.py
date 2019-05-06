# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:50:36 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@authores: 
        Prof. Dr. Denis C. L. Costa
        Prof. Ms. Maurício Maia Ribeiro
        
        Discentes:
            Heictor Alves de Oliveira Costa
            Diego Yukio Nakashima
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Aplicações de Interpolação Cúbica
        
Nome do sript: temperatura_densidade

Disponível em:


"""
# Bibliotecas Utilizadas

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

temper = np.array([-10.0, 0.0, 10.0, 20.0, 30.0, 40]);
print('Temperatura =', temper)

dens = np.array([0.99815, 0.99987, 0.99973, 0.99823, 0.99567, 0.99230]);    
print('Densidade =', dens)

f = interp1d(temper, dens)
dens1 = interp1d(temper, dens, kind='cubic',fill_value="extrapolate")

temper1 = np.arange(-10.0, 40.0, 1)

temper_interpol=input('Entre com o valor de temperatura_interpol --> ')

dens_INTERPOL=abs(dens1(temper_interpol))

print('O valor INTERPOLADO de densidade é >>>', dens_INTERPOL)

plt.plot(temper, dens, 'or', temper1, f(temper1), '--k', temper1, dens1(temper1), '*g')
plt.title(' Densidade em função da Temperatura ')
plt.xlabel(' Valores da Temperatura (°C)');
plt.ylabel ( 'Valores da Densidade (g/cm³)');
plt.legend(["Dados Reais","Projeção dos Dados","Dados Interpolados"],loc=3)
plt.grid(True)
plt.show()

print('=====================================')
print('Fim do programa temperatura_densidade')
print('=====================================')