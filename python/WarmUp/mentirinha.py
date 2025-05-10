input = int(input())

def divisores(input):
    cont = 0

    for i in range(2, input - 1):
        if input % i == 0:
            cont = cont + 1
    
    if cont == 1:
        return 'sim'
    else:
        return 'nao'

print(divisores(input))
