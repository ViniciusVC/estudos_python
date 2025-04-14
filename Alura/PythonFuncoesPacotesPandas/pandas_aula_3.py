# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_3.py

# 3. TRABALHANDO COM DICIONÁRIOS

# 3.1 Criando dicionários
# Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.
# Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido como chave (key) e o segundo como valor (value).

# Lista de carros.
carros = ['Jetta Variant', 'Passat', 'Crossfox']
print(carros)

# Valores para os carros.
valores = [88078.64, 106161.94, 72832.16]
print(valores)

# retorna o indece da lista
print("retorna o indece da lista")
print(carros.index('Passat')) 

# Item de valor de mesmo index de carros.
print("Item de valor de mesmo index de carros.")
print(valores[carros.index('Passat')])

# Criando o dicionário.
print("Criando o dicionário.")
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

input("Pressione Enter para continuar...")

# Criando dicionários com zip()
list(zip(carros, valores))

# Criando um dicionario com as duas listas.
print("Criando o dicionário com ZIP.")
dados = dict(zip(carros, valores))
print(dados)