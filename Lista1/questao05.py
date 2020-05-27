print('Calcula o valor de um desconto e o total à pagar')
preco = float(input("Entre com o preço da mercadoria(ex:788.00: R$ "))
desconto = int(input("Entre com o percentual de desconto(ex:10): "))
valordesc = preco * desconto / 100
final = preco - valordesc
print('Preço original: R$', "%.2f" %preco)
print('valor do desconto: R$', "%.2f" %valordesc)
print('Preço final: R$', "%.2f" %final)
