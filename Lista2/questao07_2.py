print('Cálculo da tinta')
area = float(input("Entre com a área a ser pintada: "))
valor = float(80.00)
if area % 54 != 0:
    consumo = int(area / 54) + 1
else:
    consumo = area / 54
total = valor * consumo

print ('%d latas a um custo de %.2f' %(consumo, total))
