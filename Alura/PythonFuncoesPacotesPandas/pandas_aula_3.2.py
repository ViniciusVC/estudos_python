# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_3.2.py

# 3.2 Operações com dicionários

# Dicionario de carros valor.
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

# Valor de Passat
print(dados['Passat'])

# Exite Passat no dicionário de carros?
print('Passat' in dados)

# Exite Fuca no dicionário de carros?
print('Fusca' in dados)

# Não exite Fusca no dicionário de carros?
print('Fusca' not in dados)

input("Pressione Enter para continuar...")

# Atribuir novo item ao dicionário.
print('Atribuir novo item ao dicionário.')
dados['DS5'] = 124549.07
print(dados)

# Remove o item de chave (key) do dicionário.
print('Remove o item de chave (key) do dicionário.')
del dados['Passat']
print(dados)
