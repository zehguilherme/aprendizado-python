"""
- Criar variáveis para nome (str), idade (int)
- Altura (float) e peso (float) de uma pessoa
- Criar variável com o ano atual (int)
- Obter ano de nascimento da pessoa (baseado na idade e ano atual)
- Obter IMC da pessoa com 2 casa decimais (peso e atura da pessoa)
- Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
"""

from datetime import date

nome = 'José Guilherme'
idade = 22
altura = 1.75
peso = 55

# Obtenção do ano atual
data_atual = date.today()  # pega a data atual do sistema (formato AAA-MM-DD)

ano_atual = data_atual.year  # pega o ano atual

# Ano nascimento
ano_nascimento = ano_atual - idade

# Cáculo IMC
imc = peso/altura**2


print('{nome} tem {idade} anos, {altura} de altura e pesa {peso:.2f} Kg.'.format(nome = nome, idade = idade, altura = altura, peso = peso))
print('O IMC de {nome} é {imc:.2f}.'.format(nome = nome, imc = imc))
print('{nome} nasceu em {ano_atual}'.format(nome = nome, ano_atual = ano_atual))