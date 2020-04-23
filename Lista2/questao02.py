print('verificar se um ano é bissexto')
ano = int(input("Entre com o ano: "))
ano_string = str(ano)
comprimento = len(ano_string)
if ano_string[comprimento-1] == '0' and ano_string[comprimento-2] == '0' or ano % 4 != 0:
    print ('Não é bissexto')
else:
    print('É ano bissexto')
