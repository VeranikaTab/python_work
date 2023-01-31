# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Введите количество абузов: '))
minimum = 10000
maximum = 1
for i in range(n):
    weight = int(input('введите вес {} арбуза:'.format(i+1)))
    if minimum > weight:
        minimum = weight
    if maximum < weight:
        maximum = weight
print('Максимальный вес арбуза {}, минимальный вес арбуза {}'.format(maximum, minimum))

