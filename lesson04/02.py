# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# # Output: 13

# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

words = set(input().lower().split())
print(len(words))

# Метод lower() — это строковый метод, который возвращает новую строку полностью в нижнем регистре.
# split() Этот метод разбивает заданную строку на отдельные слова и возвращает список этих слов.