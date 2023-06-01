#Programa de test para encontrar o componente que efetivamente esta causando o erro.
print('Iniciou programa')

DSLAMAtual='';
totalDSLAM=0;
totalDSLAMErro=0;

CaboAtual='';
totalCabo=0;
totalCaboErro=0;

SecaoAtual='';
totalSecao=0;
totalSecaoErro=0;

CaixaAtual='';
totalCaixa=0;
totalCaixaErro=0;

totalModem=0;
totalModemErro=0;

alarmesDSLAM=[];
alarmesDSLAM=[];
alarmesCabo=[];
alarmesSecao=[];
alarmesCaixa=[];
alarmesModem=[];

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
with open('base_exe.csv', 'r') as base_exe:
   ler = csv.reader(base_exe);
   next(ler); #Para nao ler o cabecalho

   for linha in ler:
      #Iniciou o loop nas linhas da planilha
      i=i+1;
      print('_FOR_____________________________linha:'+str(i));
      print(linha);
      if DSLAMAtual=='':
         #Lendo o cabecalho. Ignorar.
         print('Lendo o cabecalho. Ignorar.');
      else:
         if DSLAMAtual!=linha[0]: #Nova DSLAM?
            #Iniciando analise desta DSLAM.
            totalDSLAM=totalDSLAM+1; #somar mais uma DSLAM.
            totalDSLAMErro=0; #zerar erros para esta DSLAM.
            if (totalCaboErro==0):
               #NAO existem erros neste DSLAM, nem em seus CABOS.
               print('NAO existem erros neste DSLAM('+DSLAMAtual+') , nem em seus CABOS.');
            elif func_porcent_erro(totalCaboErro,totalCabo,'caixa',DSLAMAtual):
               #Porcentagem de erros nos cabos deste DSLAM, indicam erro na DSLAM.
               print('Incluir um alarme para este DSLAM : '+ DSLAMAtual + '.');
               alarmesDSLAM.append(DSLAMAtual);
            else:
               print('Erros sao nos CABOs');
            totalCaboErro=0; #zerar erros de CABO.
         #Fim do if Nova DSLAM.

         if CaboAtual!=linha[2]: #Novo CABO?
            #Iniciando analise desta CABO.
            totalCabo=totalCabo+1; #somar mais um CABO. 
            totalCaboErro=0; #zerar erros para este CABO.
            if (totalSecaoErro==0):
               #NAO existem erros neste CABO, nem em suas SECOES.
               print('NAO existem erros neste CABO('+CaboAtual+'), nem em suas SECOES.');
            elif func_porcent_erro(totalSecaoErro,totalSecao,'cabo',CaboAtual):
               #Porcentagem de erros nos secoes deste cabo, indicam erro na CABO.
               print('incluir um alarme para esta cabo ('+CaboAtual+').');
               alarmesCabo.append(CaboAtual);
            else:
               #Porcentagem de SECOES COM erros, indicam erro na SECAO.
               print('Erros sao das SECOES');
            totalSecaoErro=0; #zerar erros de SECAO.
         #Fim do if Novo CABO
   
         if SecaoAtual != linha[4]: #Nova Secao?
            #Iniciando analise desta SECAO.
            totalSecao=totalSecao+1; #somar mais uma SECAO.
            totalSecaoErro=0; #zerar erros para este SECAO.
   
            #Verificar se ira sinalizar esta Secao.
            if (totalCaixaErro==0):
               #NAO existem erros nesta SECAO, nem em suas CAIXAS.
               print('NAO existem erros nesta SECAO('+SecaoAtual+'), nem em suas CAIXAS.');
            elif func_porcent_erro(totalCaixaErro,totalCaixa,'secao',SecaoAtual):
               #Porcentagem de erros nas CAIXAs desta SECAO, indicam erro na SECAO.
               print('-> Incluir um alarme para esta secao('+SecaoAtual+')!');
               alarmesSecao.append(SecaoAtual);
            else:
               #Porcentagem de CAIXAs com erros, indicam erro na CAIXAs.
               print('Erros sao das CAIXAs');
            totalCaixaErro=0; #zerar erros de Caixa.
         #Fim do if Nova Secao   

         if CaixaAtual != linha[6]: #Nova Caixa?
            print('Mova caixa. CaixaAtual='+CaixaAtual+', linha[6]='+ linha[6]+'.');
            #Iniciando analise desta CAIXA.
            totalCaixa=totalCaixa+1; #somar mais uma CAIXA.
            #Verificar se ira sinalizar esta CAIXA. 
            if (totalModemErro==0):
               #NAO existem erros nesta CAIXA, nem em seus MODENS.
               print('NAO existem erros nesta CAIXA('+CaixaAtual+'), nem em seus MODENS.');
            elif func_porcent_erro(totalModemErro,totalModem,'caixa',CaixaAtual):
               #Porcentagem de MODENs com erros desta CAIXA, indicam erro na CAIXA.
               print('-> Incluir um alarme para esta caixa('+CaixaAtual+')!');
               alarmesCaixa.append(CaixaAtual); 
            else:
               #Porcentagem de MODENs com erros desta CAIXA, indicam erro na MODENs.
               print('Erros sao dos MODENs');
            totalModemErro=0; #zerar erros de modem.
         #fim do if Nova Caixa

      # O modem e' sempre novo.   	 
      totalModem = totalModem+1 #somar mais um Modem 
      
      # Atualizar variaveis.
      DSLAMAtual =linha[0];
      CaboAtual = linha[2];
      SecaoAtual = linha[4];
      CaixaAtual = linha[6];
      ModemAtual = linha[8];
   
   
      #verificar se este CABO possui ERRO.
      if linha[5] == '1':
            #Esta CABO apresentou erro. 
            totalCaboErro=totalCaboErro+1; #Total de cabos com erro nesta DSLAM. 
            print('Encontrou um erro nesta CABO('+CaboAtual+').');
      else:
            print('Analizou a CABO ('+CaboAtual+') -> sem erro.');
   
      #verificar se estA Secao possui ERRO.
      if linha[5] == '1':
            #Esta SECAO apresentou erro. 
            totalSecaoErro=totalSecaoErro+1; #Total de secoes com erro nesta Cabo. 
            print('Encontrou um erro nesta Secao('+SecaoAtual+').');
      else:
            print('Analizou a Secao ('+SecaoAtual+') -> sem erro.');
       
      #verificar se estA CAIXA possui ERRO.
      if linha[7] == '1': 
         #Esta CAIXA apresentou erro.
         totalCaixaErro=totalCaixaErro+1; #Total de Caixa com erro nesta Secao. 
         print('Encontrou um erro nesta CAIXA('+CaixaAtual+').');
      else:
         print('Analizou a CAIXA ('+CaixaAtual+') -> sem erro.');
       
      #verificar se este MODEM possui ERRO.
      if linha[9] == '1': 
         #Este MODEM apresentou erro.
         totalModemErro=totalModemErro+1; #Total de MODENs com erro nesta CAIXA. 
         print('Encontrou um erro no Modem('+ModemAtual+').');
      else:
         print('Analizou o Modem (' + ModemAtual + ') -> sem erro.');
          
   #Terminou o loop nas linhas da planilha
print('===========================================================================')
print('Relatorio final')   
print('Alarmes DSLAM : '+ str(alarmesDSLAM))
print('Alarmes Cabo : '+ str(alarmesCabo))
print('Alarmes Secao : '+ str(alarmesSecao))
print('Alarmes Caixa : '+ str(alarmesCaixa))
print('Alarmes Modem : '+ str(alarmesModem))
print('Total DSLAM : '+ str(totalDSLAM))
print('Total Cabo : '+ str(totalCabo))
print('Total Secao : '+ str(totalSecao))
print('Total Caixa : '+ str(totalCaixa))
print('Total Modem : '+ str(totalModem))

print('Terminou programa')



