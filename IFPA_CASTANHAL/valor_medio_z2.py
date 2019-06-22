# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:02:54 2019

@authors: 
        Denis Carlos Lima Costa
        Heictor Alves de Oliveira Costa
        Wendel de Oliveira Castro
        João Chaves de Oliveira Neto
  
Grupo de Pesquisa: 
        Gradiente de Modelagem Matemática e
        Simulação Computacional - GM²SC
        
Tema:
       ANÁLISE E DECISÃO SOBRE A OTIMIZAÇÃO DE PREÇOS 
       EM FUNÇÃO DA TAXA DE DETERIORAÇÃO DE PRODUTOS  
       
Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/IFPA_CASTANHAL/valor_medio_z1.py
    
"""

# Bibliotecas
# Cálculo Diferencial e Integral: sympy
import sympy as sy
# Variáveis simbólicas
T,p = sy.symbols('T,p')
# Constantes
H = 3
c = 0.2
θ = 0.7
Id = 0.002
Ic = 0.2
m = 0.04109
s = 5
α = 10000
β = 1.6
## Variáveis
Ta = 0.01; Tb = 1.8
t = Ta-Tb
P = 0.5
# Demanda Anual: a --> D(p,t)= αp**(-β)*t
a = α*P**(-β)*t
print('')
print('=======================================')
print('')
# Função Z2 = f(T,p)
def Z2(T,p):
    return (0.5*p*a*T)-(s/T)-(c*a*(θ*T*sy.exp(θ*T)-sy.exp(θ*T)+1))/(T*θ**2)-\
     (0.5*H*a*(2*sy.exp(θ*T)*T*θ-2*sy.exp(θ*T)-T**2*θ**2+2)/θ**3)+\
     (0.5*a*m**2*Id/T)-(0.5*p*Ic*a*(m**2*θ**2+2*T*θ*sy.exp(θ*(T-m))-\
      2*m*θ-T**2*θ**2-2*sy.exp(θ*(T-m))+2)/T*θ**3)
# Intervalo de Integração    
T1 = 0.01; T2 = 1.8
p1 = 9; p2 = 12
# Área do Retângulo R
R = (T2-T1)*(p1-p2)
# Valor do Lucro Médio de Z2 = f(T,p) 
def Vm_L2(T,p):
    return (1/R)*sy.integrate(Z2(T,p),T,p)#, (T, T1, T2), (p, p1, p2))
print('Vm_L2(T,p) = ', Vm_L2(T,p))
#print('Valor Médio do Lucro Vm_L1 =', round(Vm_L1(T,p),2))
print('')
print('=======================================')
print(' ')
print(' --> Fim do Programa valor_medio_z2 <--')