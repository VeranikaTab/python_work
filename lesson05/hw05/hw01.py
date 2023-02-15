# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input())
n = int(input())

def Stepen(a, n):
    if n == 0:
        return 1
    if n < 0:
        return (1/Stepen(a, -n))
    if n % 2 == 0:
        return Stepen(a, n // 2) * Stepen(a, n // 2)
    else:
        return Stepen(a, n - 1) * a
print(Stepen(a, n))

# ---------------------------- 

def pow_num(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow_num(a, b + 1) * 1 / a
    return pow_num(a, b - 1) * a


print(pow_num(int(input()), int(input())))