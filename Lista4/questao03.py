import random

v1 = []
v2 = []
inter = []
c = 0
while c < 10:
    v1.append(random.randint(1, 100))
    v2.append(random.randint(1, 100))
    inter.append(v1[c])
    inter.append(v2[c])
    c += 1

print(v1)
print (v2)
print (inter)

print()
print()

v1 = [random.randint(1, 100) for c in range(10)]
v2 = [random.randint(1, 100) for c in range(10)]
inter = []
for c in zip(v1, v2):
    inter.extend(list(c))

print(v1)
print (v2)
print (inter)
