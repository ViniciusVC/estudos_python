#Programa de test para encontrar o componente que efetivamente esta causando o erro.
print('Iniciou programa')

Cabo04Atual='';
totalCabo04=0;
totalCabo04Erro=0;

Cabo03Atual='';
totalCabo03=0;
totalCabo03Erro=0;

Cabo02Atual='';
totalCabo02=0;
totalCabo02Erro=0;

Cabo01Atual='';
totalCabo01=0;
totalCabo01Erro=0;

totalRotiador=0;
totalRotiadorErro=0;

alarmesCabo04=[];
alarmesCabo04=[];
alarmesCabo03=[];
alarmesCabo02=[];
alarmesCabo01=[];
alarmesRotiador=[];

i=0

def func_porcent_erro(totalCompErro, totalComp, nivel, CompID):
   #Funcao que calcula percent de erro 
   mediaErros=totalCompErro/totalComp*100;
   if mediaErros >= 70:
      print('Alarme ', nivel, CompID)
      return True;
   else:
      return False;
#Fim da funcao


import csv
with open('base_ex.csv', 'r') as base_exe:
   ler = csv.reader(base_exe);
   next(ler); #Para nao ler o cabecalho

   for linha in ler:
      #Iniciou o loop nas linhas da planilha
      i=i+1;
      print('_FOR_____________________________linha:'+str(i));
      print(linha);
      if Cabo04Atual=='':
         #Lendo o cabecalho. Ignorar.
         print('Lendo o cabecalho. Ignorar.');
      else:
         if Cabo04Atual!=linha[0]: #Nova Cabo04?
            #Iniciando analise desta Cabo04.
            totalCabo04=totalCabo04+1; #somar mais uma Cabo04.
            totalCabo04Erro=0; #zerar erros para esta Cabo04.
            if (totalCabo03Erro==0):
               #NAO existem erros neste Cabo04, nem em seus Cabo03S.
               print('NAO existem erros neste Cabo04('+Cabo04Atual+') , nem em seus Cabo03S.');
            elif func_porcent_erro(totalCabo03Erro,totalCabo03,'Cabo01',Cabo04Atual):
               #Porcentagem de erros nos Cabo03s deste Cabo04, indicam erro na Cabo04.
               print('Incluir um alarme para este Cabo04 : '+ Cabo04Atual + '.');
               alarmesCabo04.append(Cabo04Atual);
            else:
               print('Erros sao nos Cabo03s');
            totalCabo03Erro=0; #zerar erros de Cabo03.
         #Fim do if Nova Cabo04.

         if Cabo03Atual!=linha[2]: #Novo Cabo03?
            #Iniciando analise desta Cabo03.
            totalCabo03=totalCabo03+1; #somar mais um Cabo03. 
            totalCabo03Erro=0; #zerar erros para este Cabo03.
            if (totalCabo02Erro==0):
               #NAO existem erros neste Cabo03, nem em suas SECOES.
               print('NAO existem erros neste Cabo03('+Cabo03Atual+'), nem em suas SECOES.');
            elif func_porcent_erro(totalCabo02Erro,totalCabo02,'Cabo03',Cabo03Atual):
               #Porcentagem de erros nos secoes deste Cabo03, indicam erro na Cabo03.
               print('incluir um alarme para esta Cabo03 ('+Cabo03Atual+').');
               alarmesCabo03.append(Cabo03Atual);
            else:
               #Porcentagem de SECOES COM erros, indicam erro na Cabo02.
               print('Erros sao das SECOES');
            totalCabo02Erro=0; #zerar erros de Cabo02.
         #Fim do if Novo Cabo03
   
         if Cabo02Atual != linha[4]: #Nova Cabo02?
            #Iniciando analise desta Cabo02.
            totalCabo02=totalCabo02+1; #somar mais uma Cabo02.
            totalCabo02Erro=0; #zerar erros para este Cabo02.
   
            #Verificar se ira sinalizar esta Cabo02.
            if (totalCabo01Erro==0):
               #NAO existem erros nesta Cabo02, nem em suas Cabo01S.
               print('NAO existem erros nesta Cabo02('+Cabo02Atual+'), nem em suas Cabo01S.');
            elif func_porcent_erro(totalCabo01Erro,totalCabo01,'Cabo02',Cabo02Atual):
               #Porcentagem de erros nas Cabo01s desta Cabo02, indicam erro na Cabo02.
               print('-> Incluir um alarme para esta Cabo02('+Cabo02Atual+')!');
               alarmesCabo02.append(Cabo02Atual);
            else:
               #Porcentagem de Cabo01s com erros, indicam erro na Cabo01s.
               print('Erros sao das Cabo01s');
            totalCabo01Erro=0; #zerar erros de Cabo01.
         #Fim do if Nova Cabo02   

         if Cabo01Atual != linha[6]: #Nova Cabo01?
            print('Mova Cabo01. Cabo01Atual='+Cabo01Atual+', linha[6]='+ linha[6]+'.');
            #Iniciando analise desta Cabo01.
            totalCabo01=totalCabo01+1; #somar mais uma Cabo01.
            #Verificar se ira sinalizar esta Cabo01. 
            if (totalRotiadorErro==0):
               #NAO existem erros nesta Cabo01, nem em seus MODENS.
               print('NAO existem erros nesta Cabo01('+Cabo01Atual+'), nem em seus MODENS.');
            elif func_porcent_erro(totalRotiadorErro,totalRotiador,'Cabo01',Cabo01Atual):
               #Porcentagem de MODENs com erros desta Cabo01, indicam erro na Cabo01.
               print('-> Incluir um alarme para esta Cabo01('+Cabo01Atual+')!');
               alarmesCabo01.append(Cabo01Atual); 
            else:
               #Porcentagem de MODENs com erros desta Cabo01, indicam erro na MODENs.
               print('Erros sao dos MODENs');
            totalRotiadorErro=0; #zerar erros de Rotiador.
         #fim do if Nova Cabo01

      # O Rotiador e' sempre novo.   	 
      totalRotiador = totalRotiador+1 #somar mais um Rotiador 
      
      # Atualizar variaveis.
      Cabo04Atual =linha[0];
      Cabo03Atual = linha[2];
      Cabo02Atual = linha[4];
      Cabo01Atual = linha[6];
      RotiadorAtual = linha[8];
   
   
      #verificar se este Cabo03 possui ERRO.
      if linha[5] == '1':
            #Esta Cabo03 apresentou erro. 
            totalCabo03Erro=totalCabo03Erro+1; #Total de Cabo03s com erro nesta Cabo04. 
            print('Encontrou um erro nesta Cabo03('+Cabo03Atual+').');
      else:
            print('Analizou a Cabo03 ('+Cabo03Atual+') -> sem erro.');
   
      #verificar se estA Cabo02 possui ERRO.
      if linha[5] == '1':
            #Esta Cabo02 apresentou erro. 
            totalCabo02Erro=totalCabo02Erro+1; #Total de secoes com erro nesta Cabo03. 
            print('Encontrou um erro nesta Cabo02('+Cabo02Atual+').');
      else:
            print('Analizou a Cabo02 ('+Cabo02Atual+') -> sem erro.');
       
      #verificar se estA Cabo01 possui ERRO.
      if linha[7] == '1': 
         #Esta Cabo01 apresentou erro.
         totalCabo01Erro=totalCabo01Erro+1; #Total de Cabo01 com erro nesta Cabo02. 
         print('Encontrou um erro nesta Cabo01('+Cabo01Atual+').');
      else:
         print('Analizou a Cabo01 ('+Cabo01Atual+') -> sem erro.');
       
      #verificar se este Rotiador possui ERRO.
      if linha[9] == '1': 
         #Este Rotiador apresentou erro.
         totalRotiadorErro=totalRotiadorErro+1; #Total de MODENs com erro nesta Cabo01. 
         print('Encontrou um erro no Rotiador('+RotiadorAtual+').');
      else:
         print('Analizou o Rotiador (' + RotiadorAtual + ') -> sem erro.');
          
   #Terminou o loop nas linhas da planilha
print('===========================================================================')
print('Relatorio final')   
print('Alarmes Cabo04 : '+ str(alarmesCabo04))
print('Alarmes Cabo03 : '+ str(alarmesCabo03))
print('Alarmes Cabo02 : '+ str(alarmesCabo02))
print('Alarmes Cabo01 : '+ str(alarmesCabo01))
print('Alarmes Rotiador : '+ str(alarmesRotiador))
print('Total Cabo04 : '+ str(totalCabo04))
print('Total Cabo03 : '+ str(totalCabo03))
print('Total Cabo02 : '+ str(totalCabo02))
print('Total Cabo01 : '+ str(totalCabo01))
print('Total Rotiador : '+ str(totalRotiador))

print('Terminou programa')



