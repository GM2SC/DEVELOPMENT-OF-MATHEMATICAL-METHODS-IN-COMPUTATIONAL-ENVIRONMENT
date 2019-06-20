# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:36:14 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@authors: 
        Denis C. L. Costa
        Heictor A. de Oliveira Costa
        Wendel de Oliveira Castro
        João Neto
  
Grupo de Pesquisa: 
        Gradiente de Modelagem Matemática e
        Simulação Computacional - GM²SC
        
Tema:
       ANÁLISE E DECISÃO SOBRE A OTIMIZAÇÃO DE PREÇOS 
       EM FUNÇÃO DA TAXA DE DETERIORAÇÃO DE PRODUTOS  
       
Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/IFPA_CASTANHAL/valor_otimo.py
    
"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
T,p = sy.symbols('T,p')

print('')

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

# Variáveis
T1 = 0.01; T2 = 1.8
t = T2-T1
P = 0.5

# Demanda Anual: a --> D(p,t)= αp**(-β)*t
a = α*P**(-β)*t
# Função de várias Variáveis: Z(T,p)
def Z(T,p):
    return (0.5*p*a*T)-(s/T)-(c*a*(θ*T*sy.exp(θ*T)-sy.exp(θ*T)+1))/(T*θ**2)-\
    (0.5*H*a*(2*sy.exp(θ*T)*T*θ-2*sy.exp(θ*T)-T**2*θ**2+2)/θ**3)+\
    (0.5*p*Id*a*T*(m-T+1))

# (Z(T,p), T, 1) --> (Função, variável, ordem da derivada) 
# Derivada de Z em função de T: dZ1(T,p)
def dZ1(T,p):
    return sy.diff(Z(T,p), T, 1) 
E = dZ1(T,p)

# Derivada de Z em função de p: dZ1(T,p)
def dZ2(T,p):
    return sy.diff(Z(T,p), p, 1) 
F = dZ2(T,p)

print('')

print('=======================================================')
print('Função Analisada: Z(T,p) =', Z(T,p))
print('')
print('Derivada Parcial em função de T: dZ1(T,p) =', dZ1(T,p))
print('')
print('Derivada Parcial em função de p: dZ1(T,p) =', dZ2(T,p))
print('=======================================================')

# Conjunto Solução: S
S = sy.solve((E,F))
print('Solução da Equação:')
print('=========')
print(' T =', S)
solucao = S
print('')
print('Resultado',solucao)

print('=========')
print('---> Fim do Programa valor_otimo <---')


