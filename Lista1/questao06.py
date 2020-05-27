print('Cálculo do tempo de viagem')
distancia = float(input('Entre com a distância em km: '))
velocidade = int(input('Entre com a velocidade média em km/h: '))
tempo = distancia / velocidade
print('O tempo de viagem será de aproximadamente:', '%.2f' %tempo,'horas')
