from PIL import Image, ImageFilter
import os
import csv

def z1():
    os.mkdir('obrabotka1')

    for filename in os.listdir("C:/Users/baydu/python/lab9"): #обход всех файлов
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(os.path.join("C:/Users/baydu/python/lab9", filename))
            filtered_image = image.filter(ImageFilter.SHARPEN)
            new_name = "obrabotka1/new3_" + filename
            filtered_image.save(new_name)
print(z1())

def z2():
    os.mkdir('obrabotka2')

    for filename in os.listdir("C:/Users/baydu/python/lab9"):
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join("C:/Users/baydu/python/lab9", filename))
            filtered_image = image.filter(ImageFilter.SHARPEN)
            new_name = "obrabotka2/new3_" + filename
            filtered_image.save(new_name)
print(z2())

def z3():
    with open('data.csv') as file:
        reader = csv.reader(file)
        summ = 0
        print("Нужно купить:")
        for row in reader:
            product, number, price = row
            summ += int(number) * int(price)
            print(f"{product} - {number} шт. за {price} руб.")
        print(f"Итоговая сумма: {summ} руб.")
print(z3())