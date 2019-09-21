# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:41:18 2019
Projeto de Física Aplicada às Instalações Elétricas
Professores:
    Denis C. L. Costa - Gm²SC (CNPq)
    Moacir Kuwahara
Faculdade: Faci/Wyden
"""

# Instalações Elétricas: Simulação de Projetos
# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
# Número de Dispositivos Elétricos em 127 V: n1 
# Número de Dispositivos Elétricos em 220 V: n2 
n1 = np.array([1,2,3,4,5])
n2 = np.array([1,2,3,4,5])
# Potências Elétricas em 127 V: Pe1
Pe1 = np.array([500,200,100,400,800])
# Potências Elétricas em 220 V: Pe2
Pe2 = np.array([400,300,1000,1500,900])
# Potência Total 127 V: Pt1 (Watt)
Pt1 = np.sum(Pe1)
# Potência Total 220 V: Pt2 (Watt)
Pt2 = np.sum(Pe2)
Pt = Pt1+Pt2
# Potência Média: Pm
Pm = np.mean(Pe1+Pe2)
# Tensão Elétrica: U (Volts)
U1 = 127
U2 = 220
# Cálculo da Corrente Elétrica em 127 V: i1 (Ampère)
i1 = Pt1/U1
R1 = U1**2/Pt1
Pd1 = R1*i1**2
# Cálculo da Corrente Elétrica em 220 V: i2 (Ampère)
i2 = Pt2/U2
R2 = U2**2/Pt2
Pd2 = R2*i2**2
Pd = Pd1 + Pd2
print('')
print('====================================================')
print('Potência Elétrica Total = ', Pt,'Watt')
print('Potência Elétrica Média = ', Pm,'Watt')
print('Potência Elétrica Dissipada (127 V) = ', round(Pd1,2),'Watt')
print('Potência Elétrica Dissipada (220 V) = ', round(Pd2,2),'Watt')
print('Corrente Elétrica (a 127 V) = ', round(i1,2),'Ampère')
print('Corrente Elétrica (a 220 V) = ', round(i2,2),'Ampère')
print('====================================================')
print('')
print('Condutor sugerido para essa Corrente a 127 V')
print('')
# Loop Condicional para 127V
if (i1 < 14):
    print('--> Bitola de 1.0 mm')
elif (14 <= i1 < 17): 
    print('--> Bitola de 1.5 mm')
elif (17 <= i1 < 24): 
    print('--> Bitola de 2.5 mm')
elif (24 <= i1 < 32): 
    print('--> Bitola de 4.0 mm')
elif (32 <= i1 < 41): 
    print('--> Bitola de 6.0 mm')
elif (41 <= i1 < 57): 
    print('--> Bitola de 10.0 mm')
else:
    print('Cabos Especiais') 
print('')
print('=====================================')
print('')
print('Condutor sugerido para essa Corrente a 220 V')
print('')
# Loop Condicional para 220V
if (i2 < 14):
    print('--> Bitola de 1.0 mm')
elif (14 <= i2 < 17): 
    print('--> Bitola de 1.5 mm')
elif (17 <= i2 < 24): 
    print('--> Bitola de 2.5 mm')
elif (24 <= i2 < 32): 
    print('--> Bitola de 4.0 mm')
elif (32 <= i2 < 41): 
    print('--> Bitola de 6.0 mm')
elif (41 <= i2 < 57): 
    print('--> Bitola de 10.0 mm')
else:
    print('Cabos Especiais') 
print('')
print('=====================================')
print('')
# Comportamento Gráfico para 127 V
plt.plot(n1, Pe1)
plt.scatter(n1, Pe1)
plt.title('Simulação de Instalações Elétricas - 127 V')
plt.xlabel('Número de Dispositivos')
plt.ylabel('Potências Elétricas (Watt)')
plt.grid(True)
plt.show()
print('')
# Comportamento Gráfico para 220 V
plt.plot(n2, Pe2)
plt.scatter(n2, Pe2)
plt.title('Simulação de Instalações Elétricas - 220 V')
plt.xlabel('Número de Dispositivos')
plt.ylabel('Potências Elétricas (Watt)')
plt.grid(True)
plt.show()
print('')
print('========== Fim do Programa ===========')

# Dispositivos Elétricos
#Forno de Micro Ondas = 2000
#Freezer Horizontal = 500
#Freezer Vertical = 300
#Aspirador de Pó = 600
#Geladeira Simples = 250
#Batedeira = 100
#Geladeira Duplex = 500
#Bomba de Água = 400
#Grill = 1200
#Cafeteira Elétrica (Residencial) = 600
#Impressora = 45
#Churrasqueira Elétrica = 3000
#Liquidificador = 200
#Chuveiro Elétrico = 5500
#Computador = 300
#Máquina de Lavar Louça = 1500
#Condicionador de Ar = 1400
#Máquina de Lavar Roupa = 1000
#Projetor de Slides = 200
#Secador de Cabelo= 1000
#Espremedor de Frutas = 200
#Secadora de Roupas = 3500
#Exaustor = 150
#Televisor 32'' = 110
#Ferro Elétrico = 1000
#Fogão Elétrico 2 Bocas = 3000
#Torradeira = 800
#Fogão Elétrico de 4 Bocas = 6000
#Vetilador = 100
#Forno Elétrico Pequeno= 1500



