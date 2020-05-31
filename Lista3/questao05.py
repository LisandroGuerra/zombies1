print('Calcula MDC por Euclides')

while True:
    def mdc(number1, number2):
        
        while number1 % number2 != 0:
            number1, number2 = number2, number1 % number2

        return number2
        

    number1 = int(input("Digite primeiro número: "))
    if number1 == 0:
        break
    else:
        number2 = int(input("Digite segundo número: "))
    
        print("O MDC é %d" % mdc(number1, number2))
        print()

