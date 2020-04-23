print('Qual o tipo de triangulo')
a = int(input("Entre com o primeiro lado: "))
b = int(input("Entre com o segundo lado: "))
c = int(input("Entre com o terceiro lado: "))
if a > b + c or b > a + c or c > a + b:
    print ('Não é um triângulo')
elif a == 0 or b == 0 or c == 0:
    print('Nenhum lado pode ser zero')
elif a == b and b == c:
    print('É equilátero')
elif a != b and b != c and a != c:
    print('É isósceles')
else:
    print('É escaleno')
