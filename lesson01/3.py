# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.  3   4  = 6

i = int(input("В какой вагон запрыгнули с гловы поезда:"))
j = int(input("Номер вагона:"))
if i == j:
    answer = "Вычислить нельзя"
    print(i + j - 1)
else:
    answer = i+j-1
print(answer)
