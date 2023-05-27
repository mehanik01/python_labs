def z1():
    a = int(input("Введите число для деления его на 3"))
    ostat = a % 3
    if ostat == 0:
        print("Число делится на 3")
    else:
        print("Число не делится на 3")
    return ostat
print(z1())

def z2():
    try:
        a = int(input("Введите число для деления его на 100"))
        ostat = a / 100
    except ValueError:
        print("Введите число")

    except ZeroDivisionError:
        print("Деление на ноль")
    return ostat
print(z2())

def z3():
    x, y, z = map(int, date.split("."))
    if x * y == z % 100:
        return True
    else:
        return False
date = input("Введите дату:")
if z3():
    print(f"{date}- магическая дата")
else:
    print(f"{date}- немагическая дата")
print(z3())

def z4():
        ticket = input()

        first = ticket[:len(ticket)//2]
        second = ticket[len(ticket)//2:]
        s1,s2 = 0, 0
        for i in first:
            s1 += int(i)
        for j in second:
            s2 += int(j)
        if s1 == s2 :
            print("Счастливый")
            return True
        else:
            print("Несчастливый")
            return False
print(z4())