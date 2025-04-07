

# PYTHON PARA DATA SCIENCE - NUMPY
# 1. INTRODUÇÃO AO PYTHON
# 1.1 Introdução
# Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares.
# Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assunto é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.
# 1.2 Instalação e ambiente de desenvolvimento

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python aula1.py

### Verificando versão
import sys
versoPython = sys.version
print("versao do Python : "+versoPython) 

# 1.3 Trabalhando com arrays Numpy
# Para instalar o NumPy no seu ambiente Python, rode o seguinte comando no terminal ou prompt de comando:
# pip install numpy
# Agora podemos impotar a biblioteca numpy para nosso codigo.
import numpy as np

# Numpy é a abreviação de Numerical Python.

# Carregar arquivo carros_km.txt em memoria.
km = np.loadtxt('carros_km.txt')
print(km)
input("Pressione Enter para continuar... Carregar arquivo carros_anos.txt em memoria:")

# Carregar arquivo carros_anos.txt em memoria.
anos = np.loadtxt('carros_anos.txt', dtype=int)
# Mostra o conteudo carregado do arquivo carros_km.txt.
print(anos)
input("Pressione Enter para continuar... Obtendo a quilometragem média por ano:")

### Obtendo a quilometragem média por ano
Km_media = km / (2019 - anos)
# Alguns calculos são de divisão por zero. Por isso o alerta. Mas ele roda mesmo assim.

# Kilometrs que ficaram zeradas aparecem com nan.
print(Km_media )

# Mostrar o tipo de ariavel
print("tipo de Variavel Km_media é :")
print(type(Km_media)) 