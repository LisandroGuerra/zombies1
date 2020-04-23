print('Calculo de multa de pesca')
peso = int(input("Entre com o peso de pescado em kg: "))
limite = float(50.00)
excesso = peso - limite
multa = float(4.00)
if excesso <= 0:
    excesso = 0
    multa = 0
    print ('Não excesso %.2f' %excesso,'nem tem multa %.2f' %multa)
else:
    multa = multa * excesso
    print ('O excesso foi: %.2f' %excesso,'A multa foi %.2f' %multa)
