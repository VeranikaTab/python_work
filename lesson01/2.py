# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.   20  21  22  = 32

a = int(input("Введите количество учащихся в первом классе:"))
b = int(input("Введите количество учащихся в втором классе:"))
c = int(input("Введите количество учащихся в третьем классе:"))
print(-(-a//2)+(-(-b//2))+(-(-c//2)))
