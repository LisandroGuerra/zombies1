print('Calcula anos para pais A passar a população de B')

def pop_A(anos):    
    return 80000 * (1.03) ** anos

def pop_B(anos):
    return 200000 * (1.015) ** anos

anos = 1
while pop_A(anos) < pop_B(anos):
    anos += 1
    
print("Levará %d anos" %anos)    

