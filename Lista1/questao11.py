print('Cálculo do número de dígitos de um número')
numero = int(input('Informe um número: '))
expoente = int(input('Informe um expoente: '))
operacao = numero ** expoente
digitos = len(str(operacao))
print('O resultado da operação é:', operacao)
print('O resultado tem', digitos, 'dígitos.')
