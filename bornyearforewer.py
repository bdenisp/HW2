"""
Программа запрашивает у пользователя год рождения Пушкина А.С.
Если год рождения верный, программа выдает Верно,
Если год рождений неверный, программа выдает Неверно

Программа производит проверку введенного значения. Если значение не является целым числом,
выводится сообщение о неверно введенном значении.

ПыСы: дата рождения Пушкина А.С. 06.06.1799
"""

TRUE_BORNYEAR = 1799

bornyear = 0
while not (bornyear == TRUE_BORNYEAR):
    bornyear = input("В каком году родился А.С. Пушкин?")
    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if not (bornyear == TRUE_BORNYEAR):
            print("Неверно!")
    else:
        print("Неверно введенное значение")

print ("Верно")
