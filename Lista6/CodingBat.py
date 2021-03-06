#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  if not dia_semana or feriado:
    return True    
  return False

def dormir2(dia_semana, feriado):
  return not dia_semana or feriado

# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return a_sorri == b_sorri

# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  if a == b:
    return (a + b) * 2
  return a + b

def soma_dobro2(a, b):
  return (a + b) * 2 if a == b else a + b

# D. diff21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  return abs(n - 21)

def diff21_2(n):
  return abs(n - 21) * 2 if n > 21 else abs(n - 21)

# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  if falando:
    if hora < 7 or hora > 20:
      return True
  return False

def papagaio_2(falando, hora):
  return falando and (hora < 7 or hora > 20)

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  if a + b == 10 or a == 10 or b == 10:
    return True
  return False

def dez2(a, b):
  return a + b == 10 or a == 10 or b == 10

# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  return False

def dista10_2(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  w = []
  for l in s:
    w.append(l)
  del w[n]
  return ''.join(w)


def apaga2(s, n):
  return s[:n] + s[n + 1:]


# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  if len(s) <= 1:
    return s
  else:
    w = []
    for l in s:
      w.append(l)
    w[0], w[-1] = w[-1], w[0]
    return ''.join(w)


def troca2(s):
  return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

  print ()
  print ('Oba! Hoje vou ficar dormindo 2 !')
  test(dormir2(False, False), True)
  test(dormir2(True, False), False)
  test(dormir2(False, True), True)
  test(dormir2(True, True), True)

  print ()
  print ('Alunos problema')
  test(alunos_problema(True, True), True)
  test(alunos_problema(False, False), True)
  test(alunos_problema(True, False), False)
  test(alunos_problema(False, True), False)

  print ()
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)
  
  print ()
  print ('Soma dobro 2')
  test(soma_dobro2(1, 2), 3)
  test(soma_dobro2(3, 2), 5)
  test(soma_dobro2(2, 2), 8)
  test(soma_dobro2(-1, 0), -1)
  test(soma_dobro2(0, 0), 0)
  test(soma_dobro2(0, 1), 1)

  print ()
  print ('Diff21')
  test(diff21(19), 2)
  test(diff21(10), 11)
  test(diff21(21), 0)
  test(diff21(22), 2)
  test(diff21(25), 8)
  test(diff21(30), 18)
  
  print ()
  print ('Diff21 2')
  test(diff21_2(19), 2)
  test(diff21_2(10), 11)
  test(diff21_2(21), 0)
  test(diff21_2(22), 2)
  test(diff21_2(25), 8)
  test(diff21_2(30), 18)

  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)
  
  print ()
  print ('Papagaio 2')
  test(papagaio_2(True, 6), True)
  test(papagaio_2(True, 7), False)
  test(papagaio_2(False, 6), False)
  test(papagaio_2(True, 21), True)
  test(papagaio_2(False, 21), False)
  test(papagaio_2(True, 23), True)
  test(papagaio_2(True, 20), False)

  print ()
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)
  
  print ()
  print ('Dez 2')
  test(dez2(9, 10), True)
  test(dez2(9, 9), False)
  test(dez2(1, 9), True)
  test(dez2(10, 1), True)
  test(dez2(10, 10), True)
  test(dez2(8, 2), True)
  test(dez2(8, 3), False)
  test(dez2(10, 42), True)
  test(dez2(12, -2), True)

  print ()
  print ('Dista 10')
  test(dista10(93), True)
  test(dista10(90), True)
  test(dista10(89), False)
  test(dista10(110), True)
  test(dista10(111), False)
  test(dista10(121), False)
  test(dista10(0), False)
  test(dista10(5), False)
  test(dista10(191), True)
  test(dista10(189), False)
  test(dista10(190), True)
  test(dista10(200), True)
  test(dista10(210), True)
  test(dista10(211), False)
  test(dista10(290), False)
  
  print ()
  print ('Dista 10 => 2')
  test(dista10_2(93), True)
  test(dista10_2(90), True)
  test(dista10_2(89), False)
  test(dista10_2(110), True)
  test(dista10_2(111), False)
  test(dista10_2(121), False)
  test(dista10_2(0), False)
  test(dista10_2(5), False)
  test(dista10_2(191), True)
  test(dista10_2(189), False)
  test(dista10_2(190), True)
  test(dista10_2(200), True)
  test(dista10_2(210), True)
  test(dista10_2(211), False)
  test(dista10_2(290), False)

  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('kitten', 0), 'itten') 
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')
  
  print ()
  print ('Apaga 2')
  test(apaga2('kitten', 1), 'ktten')
  test(apaga2('kitten', 0), 'itten') 
  test(apaga2('kitten', 4), 'kittn')
  test(apaga2('Hi', 0), 'i')
  test(apaga2('Hi', 1), 'H')
  test(apaga2('code', 0), 'ode')
  test(apaga2('code', 1), 'cde')
  test(apaga2('code', 2), 'coe')
  test(apaga2('code', 3), 'cod')
  test(apaga2('chocolate', 8), 'chocolat')

  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')
  
  print ()
  print ('Troca letras 2')
  test(troca2('code'), 'eodc')	    
  test(troca2('a'), 'a')
  test(troca2('ab'), 'ba')
  test(troca2('abc'), 'cba')
  test(troca2(''), '')
  test(troca2('Chocolate'), 'ehocolatC')
  test(troca2('nythoP'), 'Python')
  test(troca2('hello'), 'oellh')
  
if __name__ == '__main__':
  main()
