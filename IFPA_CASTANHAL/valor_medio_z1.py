# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:02:54 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

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
m = 1.9
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
# Função Z1 = f(T,p)
def Z1(T,p):
    return (0.5*p*a*T)-(s/T)-(c*a*(θ*T*sy.exp(θ*T)-sy.exp(θ*T)+1))/(T*θ**2)-\
    (0.5*H*a*(2*sy.exp(θ*T)*T*θ-2*sy.exp(θ*T)-T**2*θ**2+2)/θ**3)+\
    (0.5*p*Id*a*T*(m-T+1))
# Intervalo de Integração    
T1 = 0.01; T2 = 1.8
p1 = 9; p2 = 12
# Área do Retângulo R
R = (T2-T1)*(p1-p2)
# Valor do Lucro Médio de Z1 = f(T,p) 
def Vm_L1(T,p):
    return (1/R)*sy.integrate(Z1(T,p),T,p)#, (T, T1, T2), (p, p1, p2))
print('Vm_L1(T,p) = ', Vm_L1(T,p))
#print('Valor Médio do Lucro Vm_L1 =', round(Vm_L1(T,p),2))
print('')
print('=======================================')
print(' ')
print(' --> Fim do Programa valor_medio_z1 <--')