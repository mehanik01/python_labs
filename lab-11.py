def z1():
    class Restaurant:
        def __init__(self, name, kitchen):  # 2 атрибута
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):  # метод, выводящий 2 атрибута
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")

        def open_restaurant(self):  # метод, выводящий атрибут
            print(f"Ресторан {self.name} открыт!")

    newRestaurant = Restaurant("Italiani", "Итальянская")   # экземпляр
    print(newRestaurant.name)   # вывод 2х атрибутов по отдельности
    print(newRestaurant.kitchen)

    newRestaurant.describe_restaurant() # вызов методов
    newRestaurant.open_restaurant()
print(z1())


def z2():
    class Restaurant:
        def __init__(self, name, type):
            self.name = name
            self.type = type

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.type}")

        def open_restaurant(self):
            print(f"Ресторан {self.name} открыт!")

    kitchen = "Русская"

    name1 = input("Название ресторана 1: ")
    restaurant1 = Restaurant(name1, kitchen)

    name2 = input("Название ресторана 2: ")
    restaurant2 = Restaurant(name2, kitchen)

    name3 = input("Название ресторана 3: ")
    restaurant3 = Restaurant(name3, kitchen)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
print(z2())

def z3():
    class Restaurant:
        def __init__(self, name, kitchen, number1):
            self.name = name
            self.kitchen = kitchen
            self.number1 = number1

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")
            print(f"Рейтинг: {self.number1}")

        def open_restaurant(self):
            print(f"Ресторан {self.name} открыт!")

        def update_rating(self, number2):
            self.number1 = number2

    newRestaurant = Restaurant("Italiani", "Итальянская", 3.2)
    print(newRestaurant.name)
    print(newRestaurant.kitchen)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    number2 = float(input("Введите вашу оценку для ресторана: "))
    newRestaurant.update_rating(number2)
    newRestaurant.describe_restaurant()
print(z3())