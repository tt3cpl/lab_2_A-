
with open('input_7.txt', 'r') as f:
    n = f.readline() # кол-во элементов в массиве(по условию)
    l = [int(x) for x in f.readline().split()] # считывание чисел по условию.


def ex7(A):
    s = 0 # переменная для хранения текущей суммы подмассива
    maxi = 0  # переменная для хранения максимальной суммы подмассива
    for i in A: # проходим по каждому элементу списка A
        s = max(s + i, i) # обновляем текущую сумму, выбирая максимум из суммы текущего элемента и предыдущей суммы
        maxi = max(s, maxi)   # обновляем максимальную сумму, выбирая максимум из текущей суммы и предыдущего значения максимальной суммы
    return maxi

with open('output_7.txt', 'w') as f1:
    f1.write(f"{ex7(l)}")