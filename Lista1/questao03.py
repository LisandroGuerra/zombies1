print('Diga uma quantidade de horas, minutos e segundos para saber o total em segundos')
dias = int(input('Entre com o número de dias: '))
horas = int(input('Entre com o número de horas: '))
minutos = int(input('Entre com o número de minutos: '))
segundos = int(input('Entre com o número de segundos: '))
total = (dias * 24 * 60 * 60) + (horas * 60 + minutos) * 60 + segundos
print('O total em segundos é:', total)
