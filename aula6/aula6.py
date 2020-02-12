"""
Variáveis

 - Iniciam com letra, pode conter numeros, separar com '_', letras minusculas
 - Não pode iniciar com numeros

"""

nome = 'José Guilherme'  #string
idade = 22               #int
altura = 1.75            #float
e_maior = idade > 18     #bool
data_1 = '30/11/19'      #data
data_2 = True            #bool explicito (primeira letra sempre maiuscula)
peso = 55

imc = peso/altura**2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)