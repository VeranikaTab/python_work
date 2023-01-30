# Найдите сумму цифр трехзначного числа.
# in 123  out 6
# in 100  out 1

a = int(input('Введите трехзначное число: '))
sum = 0
while a > 0:
    sum = sum + a % 10
    a = a // 10
print ('Сумма цифр числа равна: ', sum)

# Найдите сумму цифр трехзначного числа.

num = int(input())
num_sum = 0

while num:
    num_sum += num % 10
    num //= 10

print(num_sum)