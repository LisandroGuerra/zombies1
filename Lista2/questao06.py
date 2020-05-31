print('Cálculo do salário líquido')
horas = float(input("Entre com as horas trabalhadas: "))
valor = float(input("Entre com o valor da hora: "))
sb = horas * valor
ir = sb * 11 / 100
inss = sb * 8 / 100
sind = sb * 5 / 100
sl = sb - ir - inss - sind
print ('Salário Bruto: \t\t R$ %.2f' %sb)
print ('- Imposto de Renda: \t R$ %.2f' %ir)
print ('- Previdência: \t\t R$ %.2f' %inss)
print ('- Sindicato: \t\t R$ %.2f' %sind)
print ('Salário Líquido: \t R$ %.2f' %sl)
