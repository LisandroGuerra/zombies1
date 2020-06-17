conta = int(input("Entre com o valor da conta: "))
pago = int(input("Entre com o valor pago: "))
notas = [50, 20, 10, 5, 2, 1]
troco = pago - conta
for nota in notas:
    while troco >= nota:
        print("Dar troco com nota de %d" %nota)
        troco -= nota
