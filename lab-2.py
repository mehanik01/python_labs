def z1():
    a = input("Введите пароль")
    b = input("Введите пароль ещё раз")
    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")
print(z1())

def z2():
    place = int(input("Введите номер вашего места"))
    if place % 2 == 0 and place < 54:
        print ("Верхнее место")
    if place % 2 != 0 and place < 54:
        print ("Нижнее место")
    if place >= 37 and place <= 54:
        print ("Боковое место")
    else:
        print("Купе-место")
print(z2())

def z3():
    year = int(input("Введите год"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print ("Год", year, "високосный")
    else:
        print ("Это год не високосный")
print(z3())

def z4():
    colorone = input("Введите название первого цвета")
    colortwo = input("Введите название второго цвета")
    if (colorone == "красный" and colortwo == "синий") or (colorone == "синий" and colortwo == "красный"):
        print("Получен фиолетовый цвет")
    if (colorone == "красный" and colortwo == "желтый") or (colorone == "желтый" and colortwo == "красный"):
        print("Получен оранжевый цвет")
    if (colorone == "синий" and colortwo == "желтый") or (colorone == "желтый" and colortwo == "синий"):
        print("Получен зелёный цвет")
    else:
        print("Невозможно смешать цвета")
print(z4())