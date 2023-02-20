# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

nums_list = [int(i) for i in input().split()]
num_min = int(input())
num_max = int(input())

print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])

# ------------------------- 2 вариант я

list_nums1 = '-5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7'
list_nums = list_nums1.split()
print(*list_nums)
min1 = int(input('введите минимальное значение -   '))
max1 = int(input('введите максимальное значение -   '))
res = []
for i in range(1, len(list_nums)):
    if int(list_nums[i]) > min1 and int(list_nums[i]) < max1:
        res.append(i)

print(res)

# ------------------------- 3 вариант

N = list(int(i) for i in input().split())
n_min, n_max = (int(input()) for _ in 'ab')
print(list(i for i in range(len(N)) if N[i] in range(n_min, n_max + 1)))

