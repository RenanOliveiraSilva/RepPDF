n = int(input())
lista = []

if n > 0 or n <= 1000:
    for i in range(n):
        linha = list(map(float, input().split()))
        lista.append(linha)

    def verificarRegras(arr):
        if arr[2] == 1:
            return 'NAO REGAR'
        else:
            if arr[0] > 30 and arr[1] < 50:
                return 'REGAR'
            else:
                return 'NAO REGAR'

    for i in range(len(lista)):
        print(verificarRegras(lista[i]))