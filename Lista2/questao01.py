print('Qual o tipo de triangulo')
side_a = int(input("Entre com o primeiro lado: "))
side_b = int(input("Entre com o segundo lado: "))
side_c = int(input("Entre com o terceiro lado: "))
if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
    print ('Não é um triângulo')
elif side_a == 0 or side_b == 0 or side_c == 0:
    print('Nenhum lado pode ser zero')
elif side_a == side_b and side_b == side_c:
    print('É equilátero')
elif side_a != side_b and side_b != side_c and side_a != side_c:
    print('É isósceles')
else:
    print('É escaleno')
