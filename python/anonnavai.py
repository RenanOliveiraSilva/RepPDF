n = int(input())
arr = []

for i in range(n * 2):
    inp = int(input())
    arr.append(inp)

def verificarPlano(arr):
    for i in range(0, len(arr), 2):
        if arr[i] > arr[i + 1]:
            if (arr[i] + arr[i + 1]) > 40:
                print('DOROTHY DECIDE E A NONNA VAI')
                
            else:
                print('DOROTHY DECIDE')
        else:
            if (arr[i] + arr[i + 1]) > 40:
                print('DAGMAR DECIDE E A NONNA VAI')
            else:
                print('DAGMAR DECIDE')
            
verificarPlano(arr)