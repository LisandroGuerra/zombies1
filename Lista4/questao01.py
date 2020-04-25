import random

n = []
c = 0
while c < 10:
    n.append(random.randint(1, 100))
    c += 1

print(n)
n.sort()
print ("Maior: ", n[9])
print ("Menor: ", n[0])

print()
print()

n = [random.randint(1, 100) for c in range(10)]
print(n)
print ("Maior: %d" % max(n))
print ("Menor: %d" % min(n))
