num = int(input("Entre com número inteiro positivo: "))

c = 1
while c * (c + 1) * (c + 2) < num:
    c = c + 1  
if c * (c + 1) * (c + 2) == num:
    print("Número %d é o produto %d*%d*%d e portanto triangular" %(num, c, c + 1, c + 2))
else:
    print("O número %d não é triangular" %(num))
