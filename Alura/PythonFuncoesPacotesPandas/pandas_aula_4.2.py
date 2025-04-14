# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_4.2.py

# 4. FUNÇÕES E PACOTES
# Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# 4.2 Definindo funções sem e com parâmetros

# Funções sem parâmetros

# função que calcula a media dos numeros 1, 2 e 3.
def media():
  valor = (1+2+3)/3
  print(valor)

media() # chamar a função.

input("______________________________Pressione Enter para continuar...")

# Funções com parâmetros

# Funçã oque calcula a media de 3 numeros passados por parametro.
def media(number_1, number_2, number_3):
  valor = (number_1 + number_2 + number_3) / 3
  print(valor)

media(1,2,3) # chamar a função.
media(23,45,67) # chamar a função.

input("______________________________Pressione Enter para continuar...")

# calcula a media de uma lista, por parametro.
def media(lista):
  valor = sum(lista) / len(lista)
  print(valor)
# esta função nã otem nenhum retorno.

media([1,2,3,4,5,6,7,8,9,10])  # chamar a função.

input("______________________________Pressione Enter para continuar...")

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    for item in dataset.items():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)

km_media(dados, 2019)