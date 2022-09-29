def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


n = int(input())
result = []

for i in range(2, (n+2)):
    if not i % 2:
        result.append(i)

resultsplit = split(result, 5)
len = len(resultsplit)
for i in range(len):
    print(resultsplit[i])




