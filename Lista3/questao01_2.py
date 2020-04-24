print('Pede valor correto de nota')

nota = float(input('Informe uma nota de 0 a 10: '))
while 0 > nota or nota > 10:
    print("Valor inválido")
    nota = float(input('Informe uma nota de 0 a 10: '))

print("Valor válido. A nota é %.1f" %nota)
