print('Pede e compara nome e senha')

nome = senha = ''

def info():
    global nome, senha
    nome = input('Informe seu nome: ')
    senha = input('Informe sua senha: ')
    return nome, senha

info()
while nome.lower() == senha.lower():
    print("Nome e senha tem que ser diferentes")
    print("tente novamente")
    info()

print("Valor válido.")
