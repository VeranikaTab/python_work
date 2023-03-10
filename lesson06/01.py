# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод (каждое число вводится с новой строки): 
# 7  -> 3 1 3 4 2 4 12
# 6  -> 4 15 43 1 15 1 
# Вывод: 3 3 2 12 
_ = input()
n = [int(i) for i in input().split()]

_ = input()
m = [int(j) for j in input().split()]

print(*[i for i in n if i not in m])

# ------------------------- 2 вариант

m_dict = {}.fromkeys(m, 1)
print([i for i in n if not m_dict.get(i)])

# ------------------------- 3 вариант Я

first = []
last = []
result = []

for elem in range(int(input('Введите количество элементов первого списка N - '))):
    a = int(input('Введите значения списка  '))
    first.append(a)

for elem in range(int(input('Введите количество элементов второго списка M - '))):
    b = int(input('Введите значения списка  '))
    last.append(b)

for elem in first:
    if elem not in last:
        result.append(elem)
print(result)
