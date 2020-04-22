print('Cálculo de dia de vida perdidos')
cigarros = int(input('Informe quantos cigarros fuma por dia: '))
anos = float(input('Informe por quantos anos fumou: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print('Perdeu %.2f' %dias_perdidos, 'dias de vida.')
