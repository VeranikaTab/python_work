# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3 Вывод: 2
# Метод str.count() возвращает количество вхождений подстроки sub в строку str в диапазоне индексов [start, end], если они переданы в метод.
# from time import time
# from random import choices

nums = [int(i) for i in input().split()]
# nums = choices(range(3000), k=2000)

# start = time()
m_dict = {}.fromkeys(nums, 0)

for j in nums:
    m_dict[j] += 1

num_count = [1 for i in m_dict.values() if not i % 2]
print(len(num_count))


# print(time() - start)

# ------------------------- 2 вариант Я

first = []
for elem in range(int(input('Введите количество элементов  '))):
    a = int(input('Введите значения списка  '))
    first.append(a)
count = 0
for i in range(len(first)):
    for j in range(i + 1, len(first)):
        if first[i] == first[j]:
            count += 1
print(count)
    










# a = input().split() или так
# first = []
# for elem in range(int(input('Введите количество элементов  '))):
#     a = int(input('Введите значения списка  '))
#     first.append(a)

# print(sum(first.count(element) - 1 for element in first) // 2)