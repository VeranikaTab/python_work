# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным
# номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# in 385916  out  yes
# in 123456  out  no

a = int(input('Введите номер билета из 6 цифр: '))
sum1 = 0
sum2 = 0
for i in range(7):
    if i > 3:
        sum1 = sum1 + a % 10
        a = a // 10
    elif i < 3:
        sum2 = sum2 + a % 10
        a = a // 10
if (sum1 == sum2):
    print ('Билет счастливый: ', sum1 ,'=', sum2)
else:
    print ('Билет не счастливый: ', sum1 ,'не равно', sum2)

    # -----------------------------------------------------
    # Счастливый билет - билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket_number = int(input())

sum_first = 0
sum_last = 0

while ticket_number:
    digit = ticket_number % 10
    if ticket_number > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket_number //= 10

print(f"The ticket is lucky: {sum_first == sum_last}")

# ----------------------------- 2 solution

ticket_num = input()
sum_first = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
sum_last = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

print(f"The ticket is lucky: {sum_first == sum_last}")