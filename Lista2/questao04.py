print('Qual o maior de 3 números')
number1 = int(input("Entre com o primeiro número: "))
number2 = int(input("Entre com o segundo número: "))
number3 = int(input("Entre com o terceiro número: "))
if number1 >= number2 and number1 >= number3:
    print('O maior é: %d' %number1)
elif number2 >= number3:
    print('O maior é: %d' %number2)
else:
    print('O maior é: %d' %number3)
