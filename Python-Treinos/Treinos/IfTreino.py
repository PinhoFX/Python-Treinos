# Ha diferentes tipos de if

# Declaraçãod e variaveis

A=11
B=10

print('A é maior que B ??')
if A > B:
    print('Yes')
else:
    print('No')

print('B é maior que A ??')
if A < B :
    print('Yes')
else:
    print('No')
    
print('Texto fora do if porque está uma linha atraz.')
print('############################################')


# Verificar se existe as letras pedidas na variavel

# Existe olá na variavel
Texto1='Olá Maria!'
if 'Olá' in Texto1:
    print('Yes')
else:
    print('No')

# Não existe na variavel o 'João'
if 'João' in Texto1:
    print('Yes')
else:
    print('No')
    


# Igualdades
    
# Teste de igualdade
if 'Olá Maria!' == Texto1:
    print('Yes')
else:
    print('No')

# Teste de igualdade para dar falso
if 'Olá Maria' == Texto1:
    print('Yes')
else:
    print('No')

print('############################################')

# Treino de Ifs dentro de Ifs
if A == 9: print('A');print('B');print('C')
elif A==11: print('D');print('E')
else: print('F');print('G')