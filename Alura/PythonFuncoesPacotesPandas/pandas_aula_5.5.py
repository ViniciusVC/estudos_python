# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_5.5.py

# 5.5 Tratamento de dados

import pandas as pd

# importar arquivo CSV
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
#print(dataset)

pd.set_option('display.max_rows', 1000) # numero maximo de linhas
pd.set_option('display.max_columns', 50) # numero maximo de colunas

# Mostrar os 5 primerios registros do dataset.
dataset.head()

dataset.info()

# Retorn lista de boleanos onde Quilometragem Nula:
dataset.Quilometragem.isna()

# Registros com Quilometragem Nula:
dataset[dataset.Quilometragem.isna()]

# Mostrar os campos nulos como 0.
dataset.fillna(0)

# altera campos nulos poe 0.
dataset.fillna(0, inplace = True)

# Mostra registros onde Zero_km == True.
dataset.query('Zero_km == True')


input("_________________________ Pressione Enter para continuar...")

# importar novamente o arquivo CSV
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

# Eliminar registros com dados nulos.
dataset.dropna(subset = ['Quilometragem'], inplace = True)