import string

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

for x in string.punctuation:
    texto = texto.replace(x, " ")

lista = []
for palavra in texto.split():
    if palavra[0] in 'python' or palavra[-1] in 'python':
        lista.append(palavra)

print(lista)

print ()
print ()

lista = [palavra for palavra in texto.split() if palavra[0] in 'python' or palavra[-1] in 'python']
print(lista)
