import string

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

for caracter in string.punctuation:
    texto = texto.replace(caracter, "")

def letras(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False

lista = []
for palavra in texto.split():
    if len(palavra) > 4 and letras(palavra):
        lista.append(palavra)

print(lista)
print(len(lista))

print()
print()

lista = [palavra for palavra in texto.split() if len(palavra) > 4 and letras(palavra)]
print(lista)
print(len(lista))
