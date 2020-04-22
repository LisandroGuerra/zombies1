print('Calcula o valor de um salário depois de um aumento percentual')
salario = float(input("Entre com o salário(ex:788.00: R$ "))
percentual = int(input("Entre com o percentual(ex:10: "))
final = salario+salario*percentual/100
print('Salário inicial: R$', "%.2f" %salario)
print('Percentual:', percentual, '%')
print('Salário final: R$', "%.2f" %final)
