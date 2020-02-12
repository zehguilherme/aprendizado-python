#tipos de dados
#type - classe que verifica o tipo de variável (int, str, etc)

print('Jose', type('10'));

print(10, type(10)); #int

print(type(25.5)) #float

print(type('teste de string')); #string

print(type(10 == 10)); #bool

print(bool('')) # cast bool

####################################################################################

# Criar cast

# qualquer valor que estiver dentro de uma string, quando convertido pra bool, se torna true
print(type('Teste string'), bool('teste cast bool'))

# cast (int)
print(type((int)('10')))

print((float('10.5')))