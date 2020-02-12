nome = 'José Guilherme'  #string
idade = 22               #int
altura = 1.75            #float
e_maior = idade > 18     #bool
data_1 = '30/11/19'      #data
data_2 = True            #bool explicito (primeira letra sempre maiuscula)
peso = 55

imc = peso/altura**2

# print(nome, 'tem', idade, 'de idade e seu imc é', imc)

# formatar float = variavel:.2f (var deixar apenas cm 2 casas decimais)

# Usando fstrings no print - não precisa se preocupar com tipos
# print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

# Format - colocar variaveis no.format na ordem de dentro dos colchetes
# Pode usar {0}, {1}, com numeros para que se possa usar em qualquer ordem a declaração
# print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))

# print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))

# Outro formato
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n = nome, i = idade, im = imc))