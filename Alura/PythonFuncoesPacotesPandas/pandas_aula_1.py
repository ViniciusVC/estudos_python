# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_1.py

### Verificando versão
import sys
versoPython = sys.version
print("versao do Python : "+versoPython) 

# 1.3 Trabalhando com dados

# Importar biblioteca Pandas
import pandas as pd

# para usar o pandas é preciso que esteja instalado no seu ambente (pip install pandas).

# para configurar a saida:
# pd.set_option('display.max_rows', 1000) # numero maximo de linhas
# pd.set_option('display.max_columns', 50) # numero maximo de colunas

# Trazer os dados de um arquivo para memoria.
dataset = pd.read_csv('db.csv', sep = ';')

print(dataset)
input("Pressione Enter para continuar...")

# Mostrar os tipos decada coluna.
print("dataset.dtypes : Mostrar os tipos decada coluna.")
print(dataset.dtypes)
input("Pressione Enter para continuar...")

# Estatisticas
print("dataset[['Quilometragem', 'Valor']].describe() : Estatisticas.")
print(dataset[['Quilometragem', 'Valor']].describe())
input("Pressione Enter para continuar...")

# Informações da base em memoria.
print("dataset.info() : Informações da base em memoria.")
print(dataset.info())
input("Pressione Enter para continuar...")