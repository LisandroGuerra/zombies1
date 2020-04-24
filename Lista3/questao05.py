print('Calcula MDC por Euclides')

while True:
    def mdc(n1, n2):
        
        while n1 % n2 != 0:
            n1, n2 = n2, n1 % n2

        return n2
        

    n1 = int(input("Digite primeiro número: "))
    if n1 == 0:
        break
    else:
        n2 = int(input("Digite segundo número: "))
    
        print("O MDC é %d" % mdc(n1, n2))
        print()

