# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_4.3.py

# 4. FUNÇÕES E PACOTES
# Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# 4.3 Definindo funções que retornam valores

# Funções que retornam um valor
def media(lista):
  valor = sum(lista) / len(lista)
  return valor

print(media([1,2,3,4,5,6,7,8]))
resultado = media([1,2,3,4,5,6,7,8])
print(resultado)

input("______________________________Pressione Enter para continuar...")

# Função que retorna 2 parametros.
def media(lista):
  valor = sum(lista) / len(lista)
  return (valor, len(lista))

print(media([1,2,3,4,5,6,7,8,9]))
resultado, n = media([1,2,3,4,5,6,7,8,9])
print(resultado)
print(n)

input("______________________________Pressione Enter para continuar...")

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

# Funçaõ retorna cada carro com sua km media.
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        result.update({item[0]:media}) 
    return result
km_media(dados, 2025)