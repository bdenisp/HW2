"""
Даты рождения:

Путин В.В.  07.10.1952
Пушкин А.С. 06.06.1799
Калашников М.Т. 10.11.1919
Есенин С.А.    03.10.1895
Трамп Д.    14.06.1946



"""

bullvictory = 1

while bullvictory:

    counttrue = 0
    countall = 0

    # Год рождения Путина В.В. 1952

    bornyear = input("В каком году родился Путин В.В.?")
    countall += 1

    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if (bornyear == 1952):
            print("Верно!")
            counttrue += 1
        else:
            print("Неверно!")
    else:
        print("Неверно введенное значение")

    # Год рождения Пушкина А.С. 1799
    bornyear = input("В каком году родился Пушкин А.С.?")
    countall += 1

    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if (bornyear == 1799):
            print("Верно!")
            counttrue += 1
        else:
            print("Неверно!")
    else:
        print("Неверно введенное значение")

    # Год рождения Калашникова М.Т. 1919
    bornyear = input("В каком году родился Калашников М.Т.?")
    countall += 1

    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if (bornyear == 1919):
            print("Верно!")
            counttrue += 1
        else:
            print("Неверно!")
    else:
        print("Неверно введенное значение")

    # Год рождения Есенина С.А. 1895
    bornyear = input("В каком году родился Есенин С.А.?")
    countall += 1

    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if (bornyear == 1895):
            print("Верно!")
            counttrue += 1
        else:
            print("Неверно!")
    else:
        print("Неверно введенное значение")

    # Год рождения Трампа Д. 1946
    bornyear = input("В каком году родился Трамп Д.?")
    countall += 1

    bulyear = bornyear.isdigit()
    if bulyear:
        bornyear = int(bornyear)
        if (bornyear == 1946):
            print("Верно!")
            counttrue += 1
        else:
            print("Неверно!")
    else:
        print("Неверно введенное значение")

    print("//////////////////////////")
    print("Статистика")
    print("Всего вопросов:", countall)
    print("Правильных ответов:", counttrue)
    print("Ошибок:", countall - counttrue)
    print("Процент правильных ответов:", 100 * counttrue / countall, '%')
    print("//////////////////////////")

    bullvictory = input('Желаете еще раз сыграть?(y=Да/Прочее = нет)')
    if bullvictory == 'y':
        bullvictory = 1
    else:
        bullvictory = 0
