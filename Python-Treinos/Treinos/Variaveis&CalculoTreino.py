# Treino de variaveis

from time import process_time_ns
from traceback import print_stack


nome = 'João'
idade = 11
altura =1.34

print('O ', nome, ' tem ', idade,' anos e mede', altura , 'centimetros')


print('###########################################################################')

num = 10
num2 = 10

val = num+num2
val2 = num-num2
val3 = num*num2
val4 = num/num2

print('A soma é de:', val)
print('A subtração é de:', val2)
print('A multiplucação é de:', val3)
print('A divisão é de:', val4)


print('###########################################################################')


nomes = {
    
        'João' : 'Ola joão!',
        'Manel' : 'Ola Manel!',
        'Joaquim' : 'Ola Joaquim!',
        'Tiago' : 'Ola Tiago!'
}

# Este comando testa se existe algum João Caso exista vai dizer o que está na frente dele na string (Olá Joao) senão vai dar que não existe
print(nomes.get('João','Não Existe esse nome na string'))
print(nomes.get('Carvalho','Não Existe esse nome na string'))


print('###########################################################################')


