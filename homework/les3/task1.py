# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(**arg):
    try:
        arg1 = int(input("Введите число "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Числовая ошибка'
    except ZeroDivisionError:
        return "Деление на ноль"
    return res
print(f'result  {div()}')