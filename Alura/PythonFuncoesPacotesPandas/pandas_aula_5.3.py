# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_5.3.py

# 5.2 Queries com DataFrames

import pandas as pd

# importar arquivo CSV
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
#print(dataset)

# Mostrar os 5 primerios registros do dataset.
dataset.head()

input("_________________________ Pressione Enter para continuar...")

dataset.Motor
dataset.Motor == "Motor Diesel"

# Retorna uma lita com coluna boleana.
select = dataset.Motor == "Motor Diesel"

select

type(select)

# Retorna todos que tem "Motor Diesel" 
dataset[select]

input("_________________________ Pressione Enter para continuar...")

dataset[(dataset.Motor == "Motor Diesel")]

input("_________________________ Pressione Enter para continuar...")

dataset[(dataset.Motor == "Motor Diesel") & (dataset.Zero_km == True)]

(dataset.Motor == "Motor Diesel") & (dataset.Zero_km == True)

dataset.query('Motor == "Motor Diesel" and Zero_km == True')