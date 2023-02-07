# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# -------- строку можно разделить на список подстрок по определенному разделителю с помощью метода .split()

chars = input().split()
dict_chars = {}.fromkeys(chars, 0)

for i in chars:
    print(f"{i}_{dict_chars[i]}" if dict_chars[i] else i, end=" ")
    dict_chars[i] += 1
    
# dict.fromkeys() - это метод класса, который возвращает новый словарь, значение по умолчанию None.
#---------------------------------------------

text = input()
result = ''
temp = {}

for i in text:
    if i in temp:
        temp[i] = temp[i] + 1
        result = result + i + '_' + str(temp[i]) + ' '
    else:
        temp[i] = 0
        result = result + i + ' '
print(result)

#---------------------------------------------
# Используйте defaultdict для подсчета вхождений символа в строку в Python
# Defaultdict присутствует в модуле collections и является производным от класса словаря.
# Его функциональность примерно такая же, как у словарей, за исключением того, что он
# никогда не вызывает KeyError, так как предоставляет значение по умолчанию для ключа,
# который никогда не существует.

from collections import defaultdict
text_1 = "a a a b c a a d c d d"
text_list = text_1.split(' ')

text_count_dict = defaultdict(int)

for text_1 in text_list:
    if text_count_dict[text_1] == 0:
        print(*(text_1), end=' ')        
        text_count_dict[text_1] += 1
    else:
        print(*(text_1,'_', text_count_dict[text_1]), end='  ')
        text_count_dict[text_1] += 1

#---------------------------------------------
