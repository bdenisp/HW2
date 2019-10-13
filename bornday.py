TRUE_BORNYEAR = 1799
TRUE_BORNDAY = 6

bornyear = input("В каком году родился А.С. Пушкин?")
bulyear = bornyear.isdigit()
if bulyear:
    bornyear = int(bornyear)
    if (bornyear == TRUE_BORNYEAR):
        bornday = input("Верно! А какой день рождения?")
        bulday = bornday.isdigit()
        if bulday:
            bornday = int(bornday)
            if (bornday == TRUE_BORNDAY):
                print("Верно!")
            else:
                print("Неверный день рождения!")
        else:
            print("Неверно введенное значение дня рождения")
    else:
        print("Неверный год!")
else:
    print("Неверно введенное значение года рождения")
