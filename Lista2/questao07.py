import math
print('Cálculo da tinta')
area = float(input("Entre com a área a ser pintada: "))
galao = int(18)
valor = float(80.00)
consumo = math.ceil(area / 3 / galao)
total = valor * consumo
print ('Latas necessárias:', consumo)
print ('Preço total: - %.2f' %total)
print ('%d latas a um custo de %.2f' %(consumo, total))
