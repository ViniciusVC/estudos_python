# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_5.2.py

# 5.2 Seleções com DataFrames

import pandas as pd

# importar arquivo CSV
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
#print(dataset)

# Mostrar os 5 primerios registros do dataset.
dataset.head()

input("_________________________ Pressione Enter para continuar...")

# Selecionando colunas

# Retrona o tipo
print(type(dataset[['Valor']]))

# Selecionando linhas - [ i : j ]
# A indexação tem origem no zero e nos fatiamentos (slices) a linha com índice i é incluída e a linha com índice j não é incluída no resultado.

# Retorna do regitro 0 ao 2.
print(dataset[0:3])

print(dataset.loc['Passat'])

print(dataset.loc[['Passat','DS5']])

print(dataset.loc[['Passat','DS5'], ['Motor','Valor']])

print(dataset.loc[:, ['Motor','Valor']])

input("_________________________ Pressione Enter para continuar...")

# Utilizando .iloc para seleções
# Seleciona com base nos índices, ou seja, se baseia na posição das informações.
print(dataset.head())

# Buscar item 1 
print(dataset.iloc[1])

# Buscar item 1 
print(dataset.iloc[[1]])

# Buscar do item 1 ao item 4
print(dataset.iloc[1:4])

# Buscar do item 1 ao item 4 apenas as colunas 0, 5 e 2.
print(dataset.iloc[1:4, [0,5,2]])

# Buscar do item 1, 42 e 22; apenas as colunas 0, 5 e 2.
print(dataset.iloc[[1, 42, 22], [0,5,2]])

# Buscar todos os itens; apenas as colunas 0, 5 e 2.
print(dataset.iloc[:, [0,5,2]])

input("_________________________ Pressione Enter para continuar...")
print("Execricio")
import pandas as pd

dados = {
    'Nome': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados)

# A ordem que definimos as seleções é indiferente:
print(dataset[['Nome', 'Ano', 'Quilometragem', 'Valor']][1:3])
print(dataset[1:3][['Nome', 'Ano', 'Quilometragem', 'Valor']])

input("_________________________ Pressione Enter para continuar...")
print("Execricio 2")

import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

print(dataset.loc[['Passat', 'DS5'],['Motor','Valor']])
print(dataset.iloc[[1, 3],[0,-1]])