# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:48:13 2019

@authors: 
        Denis C. L. Costa
        Heictor A. de Oliveira Costa
        Wendel Castro
        João Neto
  
Grupo de Pesquisa: 
        Gradiente de Modelagem Matemática e
        Simulação Computacional - GM²SC
        
Tema:
       ANÁLISE E DECISÃO SOBRE A OTIMIZAÇÃO DE PREÇOS 
       EM FUNÇÃO DA TAXA DE DETERIORAÇÃO DE PRODUTOS  
       
Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/IFPA_CASTANHAL/grafico_3D_Z1.py
  
"""
# Bibliotecas Utilizadas no programa

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['dark_background'])

# Tamanho da malha de discretização
n = 0.025 

# Dados aplicados no Modelo
H = 3
c = 0.2
θ = 0.7
Id = 0.002
Ic = 0.2
m = 1.9
s = 5
α = 10000
β = 1.6

# Variáveis envolvidas
T1 = 0.01; T2 = 1.8
t = T2-T1
p1 = 9; p2 = 12
T = np.arange(T1, T2, n)
p = np.arange(p1, p2, n)
T, p = np.meshgrid(T, p)

# Demanda Anual: a --> D(p,t)= αp**(-β)*t
a = α*p**(-β)*t

Z1 = (0.5*p*a*T)-(s/T)-(c*a*(θ*T*np.exp(θ*T)-np.exp(θ*T)+1))/(T*θ**2)-\
    (0.5*H*a*(2*np.exp(θ*T)*T*θ-2*np.exp(θ*T)-T**2*θ**2+2)/θ**3)+\
    (0.5*p*Id*a*T*(m-T+1))
    
# Representação Gráfica   
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('Tempo')
ax.set_ylabel('Preço')
ax.set_zlabel('Lucro')
ax.set_title('Lucro Total Anual')
ax.plot_surface(T,p, Z1, cmap='Spectral')






