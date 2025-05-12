import math

n = int(input())
arr = []

for i in range(3):
    linha = list(map(int, input().split()))
    arr.append(linha)

def calculaLucro(arr):
    lucro = 0
    resto = 0
    result = []

    for i in range(len(arr)):
        calc = (math.floor(n / arr[i][0])) * arr[i][1]
        
        if calc > lucro:
            lucro = calc
            resto = n - (math.floor(n / arr[i][0]) * arr[i][0])
            result = [lucro, resto]
    
    if result[1] > 0:
        for i in range(len(arr)):
            lucroResto = 0

            if arr[i][0] <= result[1]:
                calc = (math.floor(result[1] / arr[i][0])) * arr[i][1]

                if calc > lucroResto:
                    lucroResto = calc
                    resto = result[1] - (math.floor(n / arr[i][0]) * arr[i][0])
                    result = [lucro + lucroResto, resto]

    return result[0]

print(calculaLucro(arr))