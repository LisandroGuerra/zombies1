print('Cálculo de aluguel de veículo')
ki = int(input('Entre com a kilometragem inicial: '))
kf = int(input('Entre com a kilometragem final: '))
dias = int(input('Quantos dias utilizou o veículo? '))
pd = float(60.00)
pk = float(0.15)
k = kf - ki
total = (k * pk) + (dias * pd)
print('O preço por dia é de R$', '%.2f' %pd)
print('O preço por km é de R$', '%.2f' %pk)
print('Foram rodados', k,'km em', dias, 'dias')
print('O total do aluguel é de R$', '%.2f' %total)
