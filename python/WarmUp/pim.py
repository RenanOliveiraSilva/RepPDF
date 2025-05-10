n = int(input())
arr = [] 

for i in range(1, n + 1):
    if i % 4 == 0:
        arr.append('pim')
    else:
        arr.append(str(i))

print(" ".join(arr))