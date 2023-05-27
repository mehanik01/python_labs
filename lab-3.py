from random import randint

stroka = " "
print("Если захотите закончить строку, напишите stop")
while True:
    word = input("Ваше слово-")

    if word == "stop":
        break
    stroka += word + " "

print("Ваша строка:", stroka)


def pr33():
    print("Напишите слово, чтобы проверить его на редкость")
    word = input("Ваше слово-")

    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Увы, но это не очень редкое слово...")


def pr34():
    print("Математика для детей")
    correct = 0
    notcorrect = 0

    while notcorrect < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        primer = input(f"{a} + {b} = ")
        if int(primer) == a + b:
            print("Правильно!")
            correct += 1
        else:
            print("Ответ неверный...")
            notcorrect += 1

    print("Игра окончена. Правильных ответов:", correct)


pr33(), pr34()