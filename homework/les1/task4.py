#Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и
#арифметические операции

number = input('Введите число: ')
result = 9
while result:
    if str(result) in number:
        break
    result -= 1
print(result)