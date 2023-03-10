# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

s = []
for elem in range(int(input('Введите кол-во кустов в круглой грядке  '))):
    a = int(input('Введите значения числа ягод на i-ом кусте грядки -> '))
    s.append(a)
max = 0
for i in range(-1, len(s)-1):
    temp_max = s[i - 1] + s[i] + s[i + 1]
    if temp_max > max:
        max = temp_max
print(s)
print(max)

#--------------------------------------------------

def shift(s, n):
    n = -n % len(s)
    return s[n:] + s[:n]
s = []
for elem in range(int(input('Введите кол-во кустов в круглой грядке  '))):
    a = int(input('Введите значения числа ягод на i-ом кусте грядки -> '))
    s.append(a)
max = 0

for i in range(1, len(s)):
    for i in range(-3, 3):
        s = shift(s, i)
        temp_max = s[i-1]+s[i]+s[i+1]
        if temp_max > max: max = temp_max               
        else: max       
print(s)
print(max)

#---------------------------------------------------

n = []
for elem in range(int(input('Введите кол-во кустов в круглой грядке  '))):
    a = int(input('Введите значения числа ягод на i-ом кусте грядки -> '))
    n.append(a)
max = 0
for i in range(1, len(n)):

    if i < len(n)-1:
        temp_max = n[i]+n[i+1]+n[i-1]
    else:
        if n[0] >= n[-1] or n[0] <= n[-1] and n[1] >= n[-2]:
            temp_max = n[0]+n[1]+n[-1]
        if n[0] >= n[-1] and n[1] <= n[-2]:
            temp_max = n[0]+n[-2]+n[-1]
        if n[0] <= n[-1] and n[1] <= n[-2]:
            temp_max = n[-1]+n[-2]+n[0]

    max = temp_max if temp_max > max else max

print(n)
print(max)
#-----------------------------------------------



n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(n):
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
    if bush_sum > bush_max:
            bush_max = bush_sum

print(bush_max)

# ----------------------------------

n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(-1, n - 1):
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
    if bush_sum > bush_max:
            bush_max = bush_sum

print(bush_max)

# 4
# 4 1 2 3
# 4 2 1 3