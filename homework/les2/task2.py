#Для списка реализовать обмен значений соседних элементов, т.е.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().

user = input('Укажите список через пробел: ')
user_list = user.split(' ')
number = 0
while number < len(user_list[:-1]):
    user_list[number], user_list[number + 1] = user_list[number + 1], user_list[number]
    number += 2
print(user_list)