arr = []

for i in range(4):
    inp = int(input())
    arr.append(inp)

def calculaTempo(arr):
    temp = arr[0]
    result = []
    soma = 0


    soma1 = (arr[1] * temp) + (arr[2] * temp * 2)
    soma2 = (arr[1] * temp) + (arr[3] * temp * 3)
    soma3 = (arr[2] * temp * 2) + (arr[3] * temp * 3)
    
    result.append(soma1)
    result.append(soma2)
    result.append(soma3)
    
    order = sorted(result)

    return order[2]

print(calculaTempo(arr))