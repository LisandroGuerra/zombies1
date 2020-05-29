print('Qual o maior e o menor de 3 números')
number1 = int(input("Entre com o primeiro número: "))
number2 = int(input("Entre com o segundo número: "))
number3 = int(input("Entre com o terceiro número: "))
if number1 >= number2 and number1 >= number3:
    maior = number1
elif number2 >= number3:
    maior= number2
else:
    maior = number3
if number1 <= number2 and number1 <= number3:
    menor = number1
elif number2 <= number3:
    menor= number2
else:
    menor = number3
print ('O maior é ', maior,'e o menor é ', menor)
