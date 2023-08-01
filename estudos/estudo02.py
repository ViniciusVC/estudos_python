# Aula de Python 02
# Tutorial Machine Learning Com Python
# Problema : Classificar animais
print('Iniciando variaveis')

# coluna1 : Pelo longo? (R: 0 ou 1)
# coluna2 : Perna curta? (R: 0 ou 1)
# coluna3 : Faz auau? (R: 0 ou 1)

porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1,1,0]
cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]


treino_x = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
# Informe para o modelo o que lhe foi dado, quer ele deve aprender: 1=portco 0=cachorro
treino_y = [1,1,1,0,0,0] 

#===================================================


print('Executando TREINO do modelo')
# A classe LinearSVC implementa um algoritmo de classificacao, o SVM (Maquina de Vetores de Suporte).
# O que esse algoritmo faz e encontrar uma linha que separe as classes.

# Importar a biblioteca sklearn.svm (Maquina de Vetores de Suporte)
from sklearn.svm import LinearSVC 
modelo = LinearSVC() # Instanciou o SVM
modelo.fit(treino_x, treino_y) # Executando TREINO do modelo

#===================================================

# Primeiro teste.
print('Primeiro teste:')
animal_misterioso = [1,1,1]
print(modelo.predict([animal_misterioso]))


#===================================================

# Segundo teste.
print('Segundo teste:')
misterio1=[1,1,1]
misterio2=[1,1,0]
misterio3=[0,1,1]
teste_x = [misterio1,misterio2,misterio3]
teste_y = [0,1,1]
previsoes = modelo.predict(teste_x)
print(previsoes)

#===================================================

# Importar biblioteca sklearn.metrics (TAXA DE ACERTO).
print('Taxa de Acerto:')
from sklearn.metrics import accuracy_score 
print(accuracy_score(teste_y, previsoes))

#===================================================

# Importar biblioteca PANDAS (Manipula tabela).
print('Importando Pandas.')
import pandas as pd
uri = "dadosExemploGui.csv" # Instanciar caminho do arquivo.
dados = pd.read_csv(uri) #  Obter arquivo
dados.head() # Ler conteudo do arquivo
	
#===================================================
print("X")
x=dados[["home","how_it_works","contact"]]
print(x.head())

print("Y")
y=dados["bought"]
print(y.head())

#===================================================

print("Usando o Pandas para plotar um grafico")
x.home.plot(kind='hist') # Mostar um historiograma (Grafico de barras)
print("Não faz nada porque não da pra plotar grafico neste ambiente.")


