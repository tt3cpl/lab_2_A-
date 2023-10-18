total=0
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    global total  # Используем глобальную переменную total для подсчета инверсий
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            
        else:
            result.append(right[j])
            j += 1
            total += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])
    return result



with open('input_1.txt', 'r') as f:
    n = int(f.readline())
    array = list(map(int, f.readline().split()))


sorted_array = merge_sort(array)

with open('output_3.txt', 'w') as f1:
    f1.write(str(total))

