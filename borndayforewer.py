"""
Программа запрашивает у пользователя год рождения Пушкина А.С.
Если год рождения верный, программа выдает Верно,
Если год рождений неверный, программа выдает Неверно

Программа производит проверку введенного значения. Если значение не является целым числом,
выводится сообщение о неверно введенном значении.

ПыСы: дата рождения Пушкина А.С. 06.06.1799
"""

# определение констант
TRUE_BORNYEAR = 1799
TRUE_BORNDAY = 6

# определение переменных
bornyear = 0
bornday = 0

while not (bornday == TRUE_BORNDAY):

    while not (bornyear == TRUE_BORNYEAR):

        bornyear = input("В каком году родился А.С. Пушкин?")
        bulyear = bornyear.isdigit()

        if bulyear: #проверка нат правильность ввода
            bornyear = int(bornyear)
            if not (bornyear == TRUE_BORNYEAR):
                print("Неверно!")
        else:
            print("Неверно введенное значение года рождения!")
        print ("Год рождения верный!")

    bornday = input("Какого числа родился А.С. Пушкин?")
    bulday = bornday.isdigit()

    if bulday: #проверка на правильность ввода
        bornday = int(bornday)
        if not (bornday == TRUE_BORNDAY):
            print("Неверно!")
    else:
        print("Неверно введенное значение дня рождения!")

print ("Верно!")
