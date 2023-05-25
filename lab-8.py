from PIL import Image, ImageDraw, ImageFont

def z1():
    image1 = Image.open("otkr1.jpg")
    crop_image1 = image1.crop((45, 45, 400, 400))
    crop_image1.save("crop_otkr1.jpg")
print(z1())

def z2():
    holiday = {
        "День рождения": "hb.jpg",
        "Новый год": "ny.jpg",
        "8 марта": "march.jpg"
    }

    name = input("Выберите праздник: День рождения, Новый год или 8 марта: ")
    holidayname = holiday.get(name)

    if holidayname:
        image2 = Image.open(holidayname)
        image2.show()
    else:
        print("Такой открытки нет")
print(z2())

def z3():
    image3 = Image.open("otkr1.jpg")
    crop_image3 = image3.crop((45, 45, 400, 400))
    name = input('Кого Вы хотите поздравить? ')
    draw = ImageDraw.Draw(crop_image3)

    font = ImageFont.truetype('arial.ttf', 25)
    text_color = (230,193,91)
    text_position = (70, 300)

    text = name + ', поздравляю!'
    draw.text(text_position, text, font=font, fill=text_color)
    crop_image3.save('name_image3.png')
print(z3())

