disp('===================================================================')
fprintf('\nA interpolação Numérica de 3ª Ordem Aplicada na Resolução')
fprintf('\nde Problemas das Engenharias via Modelagem Computacional ')
fprintf('\nAutores: Hugo da Silva, Maurício Ribeiro, Denis C. L. Costa,')
fprintf('\n         Heictor Costa & Lucas Pompeu')
fprintf('\nGrupo de Pesquisa: GM²SC - gm2sc.ananindeua@ifpa.edu.br')
fprintf('\nGRADIENTE DE MODELAGEM MATEMÁTICA E SIMULAÇÃO COMPUTACIONAL')
fprintf('\nINSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO PARÁ - IFPA')
fprintf('\n              Campus Ananindeua')
fprintf('\nwebsite: http://ananindeua.ifpa.edu.br')
fprintf('\nDisponível em: https://github.com/GM2SC/DEVELOPMENT-OF-')
fprintf('\nMATHEMATICAL-METHODS-IN-COMPUTATIONAL-ENVIRONMENT/blob/')
fprintf('\nmaster/CONBREPRO2019/calculoz.m\n\n')
disp('===================================================================')
%%
fprintf('\n>>>>>>>>>>>>>>> PROGRAMA 03 - calculoz <<<<<<<<<<<<<<<<\n\n')
disp('') 
% Vetor z
z = [0.000 0.025 0.050 0.100 0.150 0.200 0.250 0.300 0.350 0.400 0.450 0.500...
     0.550 0.600 0.650 0.700 0.750 0.800 0.850 0.900 0.950 1.000 1.100 1.200...
     1.300 1.400 1.500 1.600 1.700 1.800 1.900 2.000 2.200 2.400 2.600 2.800];
a = length(z)
% Vetor erf
erfz = [0.0000 0.0282 0.0564 0.1125 0.1680 0.2227 0.2763 0.3286 0.3794 0.4284 0.4755 0.5202...
        0.5633 0.6039 0.6420 0.6778 0.7112 0.7421 0.7707 0.7970 0.8209 0.8427 0.8802 0.9103...
        0.9340 0.9523 0.9661 0.9763 0.9838 0.9891 0.9928 0.9953 0.9981 0.9993 0.9998 0.9999]; 
b = length(erfz)
z1 = [0: 0.1 :2.8];
erfz1 = spline(z,erfz,z1);
z_interpol=input('Entre com o valor de z_interpol --> ');
disp('O valor INTERPOLADO de erf é  >>>')
ERF_INTERPOL=abs(spline(z,erfz,z_interpol));
formatSpec = 'ERF_INTERPOL = %4.4f \n';
fprintf(formatSpec,ERF_INTERPOL)
disp('Tecle para visualizar o gráfico')
pause
figure (1)
plot (z,erfz,'og',z1,erfz1,'b',z,erfz,'*k');
title (' ERF em função de Z ');
xlabel(' Valores de z ');
ylabel ( 'Valores de erf(z)');
text(z_interpol,ERF_INTERPOL, '\leftarrow erf(z)')
% legend('ERF INTERPOL','Z')
axis([0,3,0,1]);
grid on