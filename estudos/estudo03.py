# Aula de Python 03
# Tutorial Machine Learning Com Python
# Problema : Visitantes do site que acessam home, how_it_works e contact.

# Importar biblioteca PANDAS (Manipula tabela).
print('Importando Pandas, para ler tabela csv.')
import pandas as pd
uri = "dadosExemploGui.csv" # Instanciar caminho do arquivo.
dados = pd.read_csv(uri) # Instanciar 
dados.head() #Ler informações

#===================================================

print("X")
x=dados[["home","how_it_works","contact"]]
print(x.head())

print("Y")
y=dados["bought"]
print(y.head())

#===================================================

print("Importar a bibliotecas")
#sklearn.svm (Modelo linear - Maquina de Vetores de Suporte)
from sklearn.svm import LinearSVC 

#train_test_split (separa os treinos e testes.)
from sklearn.model_selection import train_test_split 

modelo = LinearSVC() # Instanciou o SVM

treino_x, teste_x, treino_y, teste_y = train_test_split(x,y)
# separa os treinos e testes.

modelo.fit(treino_x, treino_y) # treina modelo

# Primeiro teste do modelo.
previsoes = modelo.predict(teste_x)

print('Importar biblioteca sklearn.metrics (TAXA DE ACERTO).')
from sklearn.metrics import accuracy_score 
print('TAXA DE ACERTO:')
print(accuracy_score(teste_y, previsoes)*100)

