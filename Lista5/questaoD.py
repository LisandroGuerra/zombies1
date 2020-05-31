counter = 0
for i in range(18644, 33088):
    if '2' in str(i) and '7' not in str(i):
        counter += 1

print (counter)

# print (len([i for i in range(18644, 33088) if '2' in str(i) and '7' not in str(i)]))
