conta = int(input("Entre com o valor da conta: "))
pago = int(input("Entre com o valor pago: "))
troco = pago - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print("Dar troco com nota de %d" %nota)
        troco -= nota
