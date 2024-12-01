# 1. Создаем функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # 2. Создаем переменную str_number и записываем строковое
    # представление (str) числа number в нее.
    str_number = str(number)
    if len(str_number) > 1:
        # Отделение первой цифры в числе: создание переменной first
        first = int(str_number[0])
        # Возвращайте значение first
        return first * get_multiplied_digits(int(str_number[1:]))

    else:
        return int(str_number)



result = get_multiplied_digits(40203)
print(result)


def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])

        return first + get_multiplied_digits(int(str_number[1:])) #Все то же только +
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)