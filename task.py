#задача 30
def func(q, k, m):
    lis = []
    for i in range(q, (q+(m-1)*k)+1, k):
        lis.append(i)
    print(lis)

q = int(input('Введите начальное число последовательности: '))
k = int(input('Введите шаг последовательности: '))
m = int(input('Введите количество элементов последовательности: '))

func(q, k, m)

#задача 32

def func(lis, q, k):
    new = []
    for i in range(len(lis)):
        if q < lis[i] < k:
            new.append(lis[i])
    print(new)
lis = [-10, -9, -8, -7, -6, -5, -44, -3, -2, -10, 0, 12, 2, 3, 41, 5, 6, 73, 8, 9, 10]
q = int(input('Введите начальное число последовательности: '))
k = int(input('Введите максимальное число последовательности: '))

func(lis, q, k)