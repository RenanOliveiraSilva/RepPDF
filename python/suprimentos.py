n = int(input())
arr = []

if n > 0 and n <= 1000:
    for i in range(n):
        inp = str(input())
        arr.append(inp)
        
    def calculaSupri(arr):
        diff = []
        saldo = 0

        for i in range(len(arr)):
            saldo = saldo + int(arr[i])

            if saldo < 0:
                diff.append(saldo)

        order = sorted(diff)
        
        return (order[0] * (-1))

print(calculaSupri(arr))