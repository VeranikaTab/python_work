# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = []
for elem in range(int(input('Введите n - кол-во элементов первого множества  '))):
    a = int(input('Введите значения элементов множества n '))
    n.append(a)
m = []
for elem in range(int(input('Введите m - кол-во элементов первого множества  '))):
    a = int(input('Введите значения элементов множества m '))
    m.append(a)

print(*sorted((set(n).intersection(set(m)))))
