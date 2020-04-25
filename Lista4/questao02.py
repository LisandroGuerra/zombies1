import random

n = []
par = []
impar = []
c = 0
while c < 20:
    n.append(random.randint(1, 100))
    if n[c] % 2 == 0:
        par.append(n[c])
    else:
        impar.append(n[c])
    c += 1

print(n)
print ("Pares: ", par)
print ("Impares: ", impar)

print()
print()

n = [random.randint(1, 100) for c in range(20)]
par = [p for p in n if p % 2 == 0]
impar = [i for i in n if i % 2 ==1]
print(n)
print ("Pares: ", par)
print ("Impares: ", impar)

