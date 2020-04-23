print('Qual o maior e o menor de 3 números')
n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
n3 = int(input("Entre com o terceiro número: "))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior= n2
else:
    maior = n3
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n3:
    menor= n2
else:
    menor = n3
print ('O maior é ', maior,'e o menor é ', menor)
