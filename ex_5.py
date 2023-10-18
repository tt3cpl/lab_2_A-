def fme(arr):
    can = None
    total = 0

    for e in arr:
        if total == 0:
            can = e
            total = 1
        elif can == e:
            total += 1
        else:
            total -= 1

    total = 0
    for e in arr:
        if e == can:
            total += 1

    if total > n // 2:
        return 1
    else:
        return 0
    
with open('input_5.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

result = fme(arr)

with open('output_5.txt', 'w') as f1:
    f1.write(str(result))