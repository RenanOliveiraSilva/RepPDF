nums = {
    '*': 0,
    '.': 1,
    '-': 5,
}

n = str(input())
j = '' 
lista = []
lista.append([n])

while j != '*':
    linha = list(map(str, input().split()))
    lista.append(linha)
    if linha == ['*'] :
        j = str(linha[0])

for i in range(len(lista)):
    numDecimal = 0
    cont = len(lista[i])
    for j in range(len(lista[i])):
        print(lista[i][j])
    
    # print(numDecimal)