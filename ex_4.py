def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


with open('input_4.txt', 'r') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().split()))
    k = int(f.readline())
    targets = list(map(int, f.readline().split()))

indices = []
for target in targets:
    index = binary_search(array, target)
    indices.append(index)

with open('output_4.txt', 'w') as f1:
    for index in indices:
        f1.write(str(index) + ' ')
