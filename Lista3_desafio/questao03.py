num = int(input("Entre com número inteiro positivo: "))
if num == 2:
    print ("Primo")
elif num % 2 == 0:
    print("Composto")
else:
    x = 3
    for x in range(3, num + 1):
        if num % x == 0:
            if num != x:
                print("Composto")
            else:
                print ("Primo")
