# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:57:48 2019

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
        Derivada de uma Função com uma variável independente
        
Nome do sript: derivadas

Disponível em: 
    

"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x = sy.symbols('x')

print('')

# Função de uma Variável: f(x)
def f(x):
    return 2*x**3 - 5*x**2

# (f(x), x,1) --> (Função, variável, ordem da derivada) 
# Derivada 1ª da Função: df1(x)
def df1(x):
    return sy.diff(f(x), x,1) 
# Derivada 2ª da Função: df2(x)
def df2(x):
    return sy.diff(f(x), x,2) 
print('')
print('=======================================')
print('Função Analisada: f(x) =', f(x))

print('Derivada 1ª da Função: df1(x) =', df1(x))

print('Derivada 2ª da Função: df2(x) =', df2(x))

print('=======================================')
print('')
# Valor Numérico das Derivadas 
print('Valor Numérico da Derivada 1ª')
VN_df1 = df1(x).subs(x,3)
print('VN_df1 =', VN_df1)

print('')
print('Valor Numérico da Derivada 2ª')
VN_df2 = df2(x).subs(x,-1)
print('VN_df2 =', VN_df2)

print('')
print('---> Fim do Programa derivadas <---')

