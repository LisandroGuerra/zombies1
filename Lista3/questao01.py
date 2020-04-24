print('Pede valor correto de nota')

notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
valida = False
nota = int(input('Informe uma nota de 0 a 10: '))

while valida == False:
    if nota in notas:
       print("Valor válido. A nota é %d" %nota)
       valida = True
    else:
        print("Valor inválido")
        nota = int(input('Informe uma nota de 0 a 10: '))
