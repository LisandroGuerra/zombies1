print('Qual o maior de 3 números')
n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
n3 = int(input("Entre com o terceiro número: "))
if n1 >= n2 and n1 >= n3:
    print('O maior é: %d' %n1)
elif n2 >= n3:
    print('O maior é: %d' %n2)
else:
    print('O maior é: %d' %n3)
