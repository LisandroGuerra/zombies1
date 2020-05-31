print('Calcula série de Fibonacci para número')

while True:
    def fibonacci(num):
        global x, y, z # não faz parte deste exercicio feito para teste
        k = 0
        x, y = 0, 1
        while k < num:
            z = y
            x, y = y, x + y
            k += 1

        return z
        

    num = int(input("Digite um número: "))
    if num == 0:
        break
    else:
        print("O número de Fibonacci de %d é %d" % (num, fibonacci(num)))
        print(y)# não faz parte deste exercicio feito para teste

