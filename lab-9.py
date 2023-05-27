from PIL import Image, ImageFilter
import os
import csv

def z1():
    os.mkdir('obrabotka1')

    for filename in os.listdir("C:/python_labs/img"): #обход всех файлов
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(os.path.join("C:/python_labs/img", filename))
            filtered_image = image.filter(ImageFilter.SHARPEN)
            new_name = "obrabotka1/new3_" + filename
            filtered_image.save(new_name)
z1()

def z2():
    os.mkdir('obrabotka2')

    for filename in os.listdir("C:/python_labs/img"):
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join("C:/python_labs/img", filename))
            filtered_image = image.filter(ImageFilter.SHARPEN)
            new_name = "obrabotka2/new3_" + filename
            filtered_image.save(new_name)
z2()

def z3():
    file_path ="C:/python_labs/123.csv"
    with open(file_path) as f:
        total_cost = 0
        print('Нужно купить: ')
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            prise = int(row[2])
            cost = quantity * prise
            total_cost += cost
            print(f'{product} - {quantity} шт за {prise} руб')
    print(f'Итоговая стоимость: {total_cost} руб')
z3()