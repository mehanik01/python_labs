from random import randint

def z1():
    l= ["1", "3", "6", "8", "9"]
    proverka = input("Введите число, чтобы проверить, входит ли оно в список")
    if proverka in l:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Такого числа нет")
print(z1())


def z2():
    l = [randint(1, 100) for i in range(5)]
    proverka = input("Введите число, чтобы проверить, входит ли оно в рандомный список")
    if proverka in l:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Такого числа нет")
print(z2())


def z3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    day = int(input("Сколько выходных Вы хотите?"))
    for i in week:
        print("Ваши рабочие дни:", *week[:-day])
        print("Ваши выходные дни:", *week[-day:])
        break
print(z3())


def z4():
    t = input("Чтобы узнать список нажмите любую кнопку")
    one = ["Петров", "Снегова", "Лебедева"]
    two = ["Иванов","Махонина","Зайцева"]
    team = tuple(one[:2] + two[:2])
    print("Группа 1:", *one)
    print("Группа 2:", *two)
    print("Спортивная команда:", *team)
    print("Количество спортсменов: ", len(team))
    team2 = sorted(team)
    print("Список команды по алфавиту:", *team2)
    item = "Иванов"
    if item in team2:
        print("Иванов входит в команду")
    else:
        print("Иванов не входит в команду")
    count = team2.count("Иванов")
    print("Количество появлений в списках:", count)
print(z4())