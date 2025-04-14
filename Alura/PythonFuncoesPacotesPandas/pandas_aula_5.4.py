# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_5.4.py

# 5.4 Iterando com DataFrames

import pandas as pd

# importar arquivo CSV
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
#print(dataset)

# Mostrar os 5 primerios registros do dataset.
dataset.head()

input("_________________________ Pressione Enter para continuar...")

# Rotulos das colinas com for:
for item in dataset:
  print(item)

# Rotulos das colunas da forma correta:
print(list(dataset.iterrows()))

input("_________________________ Pressione Enter para continuar...")
# Rotulos das colunas da forma correta:
print(list(dataset.columns))

input("_________________________ Pressione Enter para continuar...")

for index, row in dataset.iterrows():
  if(2019 - row['Ano'] != 0):
    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
  else:
    dataset.loc[index, 'Km_media'] = 0