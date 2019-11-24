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
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/INTERPOLATION/temperatura_densidade.py


"""
# Bibliotecas Utilizadas
from time import sleep
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
print('')
print('=================================================================')
print('')
print('====================== Início do Programa =======================')
print('')
print('Grandezas Envolvidas >>>')
print('')
# Matriz da Temperatura
temper = np.array([-10.0, 0.0, 10.0, 20.0, 30.0, 40]);
print('Temperatura =', temper,'°C')
print('')
dens = np.array([0.99815, 0.99987, 0.99973, 0.99823, 0.99567, 0.99230]);    
print('Densidade =', dens, 'g/cm³')
print('')
# Função de Interpolação Spline Cúbica
f = interp1d(temper, dens)
dens1 = interp1d(temper, dens, kind='cubic',fill_value="extrapolate")
temper1 = np.arange(-10.0, 40.0, 1)

# Novo valor da Temperatura
print('Dado de Entrada >>>')
temper_interpol=input('Entre com o valor de temperatura_interpol (°C) --> ')
print('')
print('Dado de Saída >>>')
print('')
dens_INTERPOL=abs(dens1(temper_interpol))
print('O valor INTERPOLADO da Densidade é (g/cm³) >>>', dens_INTERPOL)
print('')
print('Representação Gráfica da Spline Cúbica')
print('')
sleep (10)
plt.figure(1)
plt.plot(temper, dens, 'or', temper1, f(temper1), '--k', temper1, dens1(temper1), '*g')
plt.title(' Densidade em função da Temperatura ')
plt.xlabel(' Valores da Temperatura (°C)');
plt.ylabel ( 'Valores da Densidade (g/cm³)');
plt.legend(["Dados Reais","Projeção dos Dados","Dados Interpolados"],loc=3)
plt.grid(True)
plt.show()
sleep (3)
print('======================== Fim do Programa ========================')
print('')
print('=================================================================')





