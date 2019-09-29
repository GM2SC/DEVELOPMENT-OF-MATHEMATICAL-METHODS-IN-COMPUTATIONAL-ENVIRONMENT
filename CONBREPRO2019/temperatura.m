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
fprintf('\nmaster/CONBREPRO2019/temperatura.m\n\n')
disp('===================================================================')
%%
fprintf('\n>>>>>>>>>>>>>>>>> PROGRAMA 01 <<<<<<<<<<<<<<<<<<<\n\n')
disp('') 
% Vetor Temperatura 
temper = [-10.0000 0.0000 10.0000 20.0000 30.0000];
b = length(temper);
% Vetor Densidade
dens = [0.99815 0.99987 0.99973 0.99823 0.99567];    
a = length(dens);
% Vetor interpolado
temper1 = [-10.0000: 0.01 :30.0000];
dens1 = spline(temper,dens,temper1);
temper_interpol=input('Entre com o valor de temperatura_interpol --> ');
disp('O valor INTERPOLADO de densidade é  >>>')
dens_INTERPOL=abs(spline(temper,dens,temper_interpol));
formatSpec = 'dens_INTERPOL = %12.8f \n'; 
fprintf(formatSpec,dens_INTERPOL)
disp('Tecle para visualizar o gráfico')
pause
figure (1)
plot (temper,dens,'g',temper1,dens1,'b',temper,dens,'ro');
title (' densidade em função da temperatura ');
xlabel(' Valores de temperatura ');
ylabel ( 'Valores de densidade');
text(temper_interpol,dens_INTERPOL, '\leftarrow dens=f(temp)')
grid on