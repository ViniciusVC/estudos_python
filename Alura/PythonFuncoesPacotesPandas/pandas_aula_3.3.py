# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_3.3.py

# 3.3 Métodos de dicionários

# Dicionario de carros valor.
dados = {'Jetta Variant': 88078.64, 'Crossfox': 72832.16, 'DS5': 124549.07}
print(dados)

# Atualiza o dicionário.
print('Atualiza o dicionário.')
dados.update({'Passat': 106161.94})
print(dados)

# Atualiza Passat e inclui Fusca.
dados.update({'Passat': 106161.95, 'Fusca': 150000})
print('inclui Fusca')
print(dados)

input("Pressione Enter para continuar...")

# Cria uma cópia do dicionário.
dadosCopy = dados.copy()
del dadosCopy['Fusca']
print('dadosCopy:')
print(dadosCopy)
print('dados:')
print(dados)

input("Pressione Enter para continuar...")

# Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como default é retornado. Se o valor default não for fornecido e a chave não for encontrada no dicionário um erro será gerado.
print(dadosCopy.pop('Fusca', 'Chave não encontrada'))
print(dadosCopy.pop('DS5', 'Chave não encontrada'))

input("Pressione Enter para continuar...")

# Remove todos os itens do dicionário.
dadosCopy.clear()
print('Apagado o dadosCopy:')
print(dadosCopy)

