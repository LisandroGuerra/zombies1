print('Cálculo de dia de vida perdidos')
cigarros = int(input('Informe quantos cigarros fuma por dia: '))
anos = float(input('Informe por quantos anos fumou: '))
tempo = float(1 / 6 / 24)
perde = anos * 365 * cigarros * tempo
print('Perdeu', '%.2f' %perde, 'dias de vida.')
