print('Calcula série de Fibonacci para número')

def fibonacci(num):    
    if num <= 1:
        return num
    else:
        return(fibonacci(num - 1) + fibonacci(num - 2))
    

num = int(input("Digite um número: "))
print (fibonacci(num))

