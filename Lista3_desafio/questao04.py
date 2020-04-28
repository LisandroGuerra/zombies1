num = int(input("Entre com número inteiro positivo: "))
for x in range(2, num):
  while num % x == 0:
    print (num, '|', x)
    num /= x
