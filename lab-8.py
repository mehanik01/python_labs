from PIL import Image, ImageDraw, ImageFont

def z1():
    image1 = Image.open("img/ny.png")
    crop_image1 = image1.crop((45, 45, 400, 400))
    crop_image1.save("img/crop_ny.png")
print(z1())

def z2():
    holiday = {
        "День рождения": "img/birthday.png",
        "Новый год": "img/ny.png",
        "8 марта": "img/march.jpg"
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
    image3 = Image.open("bobik.jpg")
    crop_image3 = image3.crop((45, 45, 400, 400))
    name = input('Кого Вы хотите поздравить? ')
    draw = ImageDraw.Draw(crop_image3)

    font = ImageFont.truetype('RubikWetPaint-Regular.ttf', 25)
    text_color = (230,193,91)
    text_position = (70, 300)

    text = name + ', поздравляю!'
    draw.text(text_position, text, font=font, fill=text_color)
    crop_image3.save('postcard.png')
print(z3())

