# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:16:47 2019

@authors Professors: 
        Dr. Denis C. L. Costa
        MSc. Lair Aguiar de Meneses
        
@authors Students:
        Heictor A. de O. Costa
        Brennus Caio
        Júlio Azancort

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Representação Gráfica de Sinais utilizando o Método de Fourier
        
Disponível em:
             
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-COMPUTATIONAL-ENVIRONMENT/blob/master/SENGI_2020/Fourier_02.py
    
"""

# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível
import numpy as np 

from numpy import *

# Biblioteca matplot: Gráficos
import matplotlib.pyplot as plt

##########################################################
# Variáveis de Controle

T0 = 0                       # Instante Inicial

T1 = 5                       # Instante Final

t = np.linspace(T0,T1,100)   # Intervalo de análise

# Declarando a Função - Sinal
def f(t):
    return 2*t

# Representação Algébrica do Sinal
print('S(n) = a0/2 + F(n)')
print('')
print('S(n) = a0/2 + Σ[an.cos(nwt) + bn.sen(nwt)]')
print('')

a0 = 10

# def F1(t):
#     return -10.0*sin(0.4*pi*t)/pi
# def F2(t):
#     return -5.0*sin(0.8*pi*t)/pi
# def F3(t):
#     return (-3.33333333333333*cos(6.0*pi)/pi + \
#            0.555555555555556*sin(pi/1125899906842624)/pi**2)*sin(1.2*pi*t) +\
#           (-0.555555555555556/pi**2 + 3.33333333333333*sin(pi/1125899906842624)/pi +\
#            0.555555555555556*cos(6.0*pi)/pi**2)*cos(1.2*pi*t)
# def F4(t):
#     return -2.5*sin(1.6*pi*t)/pi
# def F5(t):
#     return -2.0*sin(2*pi*t)/pi
# def Fn(t):
#     return F1(t) + F2(t) + F3(t) + F4(t) + F5(t)

limiteinferior = 0.0
limitesuperior = 10**(-1)
numeropontos = 100
 
ruido = random.uniform(low=limiteinferior, high=limitesuperior, size=numeropontos)
       
# def S(t):
#     return a0/2 + Fn(t)

S =  -10.0*sin(2*pi*t/5)/pi - 5.0*sin(4*pi*t/5)/pi - 3.33333333333333*sin(6*pi*t/5)/pi -\
      2.5*sin(8*pi*t/5)/pi + 5.0 # + ruido


print('S(n) é a representação do Spectro do Sinal no n-ésimo Harmômico')
print('')

# Representação Gráfica do Sinal

plt.plot(t, S, '-b', label='Série de Fourier', linewidth = 2.0)
plt.plot(t, f(t), '-r', label='Função Geradora', linewidth = 2.0)
plt.xlabel('Tempo')
plt.ylabel('Espectro do Sinal')
plt.title('Representação da série de Fourier')
plt.legend(loc=4) 
plt.grid(True)
plt.show() 

##########################################################

# Representação Gráfica do Sinal Colorido
import matplotlib.cm as cm


# The colormap
cmap = cm.jet

# Create figure and axes
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(t, S, c=S,s=10, label ='Série de Fourier', cmap=cmap, linewidth = 2.0)
plt.plot(t, f(t), '-k', label='Função Geradora', linewidth = 2.0)
plt.xlabel('Tempo')
plt.ylabel('Espectro do Sinal')
plt.legend(loc=4) 
plt.grid(True)
# plt.savefig("Series_Fourier_Color{}.png".format(n), dpi=200 )
plt.show()

##########################################################


print(' ')
print(' ===== Fim do Programa Fourier_02 ====')