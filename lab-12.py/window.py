def z1():
    class Restaurant:
        def __init__(self, name, kitchen):  #атрибуты
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):  #методы
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")
            print(f"Ресторан {self.name} открыт!")

    class IceCreamStand(Restaurant):    #наследование
        def __init__(self, name, kitchen, flavors):
            super().__init__(name, kitchen)
            self.flavors = flavors

        def spisok(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    iceCreamStand = IceCreamStand("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"])  # экземпляр

    print(iceCreamStand.name)  # вывод атрибутов
    print(iceCreamStand.kitchen)

    iceCreamStand.describe_restaurant()  # вызов методов
    iceCreamStand.spisok()  # вывод списка вкусов
print(z1())


def z2():
    input("Задача 2.1: добавление локации и времени работы")
    class Restaurant:
        def __init__(self, name, kitchen):
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")
            print(f"Ресторан {self.name} открыт!")
            print(f"Локация: {self.location}")
            print(f"Время работы: {self.time}")

    class IceCreamStand(Restaurant):
        def __init__(self, name, kitchen, flavors, location, time):
            super().__init__(name, kitchen)
            self.flavors = flavors
            self.location = location
            self.time = time

        def spisok(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    iceCreamStand = IceCreamStand("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"], "Москва", "10:00-20:00")  # экземпляр класса

    print(iceCreamStand.name)  # вывод атрибутов
    print(iceCreamStand.kitchen)
    print(iceCreamStand.location)
    print(iceCreamStand.time)

    iceCreamStand.describe_restaurant()  # вызов методов

    iceCreamStand.spisok()  # вывод списка вкусов
print(z2())


def z3():
    input("Задача 2.2: добавление и удаление вкусов")
    class Restaurant:
        def __init__(self, name, kitchen):
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")
            print(f"Ресторан {self.name} открыт!")
            print(f"Локация: {self.location}")
            print(f"Время работы: {self.time}")

    class IceCreamStand(Restaurant):
        def __init__(self, name, kitchen, flavors, location, time):
            super().__init__(name, kitchen)
            self.flavors = flavors
            self.location = location
            self.time = time

        def spisok(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

        def add(self, flavor):
            self.flavors.append(flavor)

        def remove(self, flavor):
            self.flavors.remove(flavor)

        def new_spisok(self):
            print("Новый список вкусов:")
            for flavor in self.flavors:
                print(flavor)

    iceCreamStand = IceCreamStand("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"], "Москва", "10:00-20:00")  # экземпляр класса
    print(iceCreamStand.name)  # вывод атрибутов
    print(iceCreamStand.kitchen)
    print(iceCreamStand.location)
    print(iceCreamStand.time)

    iceCreamStand.describe_restaurant()  # вызов методов
    iceCreamStand.spisok()

    new = input("Введите новый вкус для добавления: ")
    iceCreamStand.add(new)

    # Ввод вкуса для удаления
    remove = input("Введите вкус для удаления: ")
    iceCreamStand.remove(remove)

    iceCreamStand.new_spisok()
print(z3())

def z4():
    input("Задача 2.3: проверка наличия вкуса")
    class Restaurant:
        def __init__(self, name, kitchen):
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")
            print(f"Ресторан {self.name} открыт!")
            print(f"Локация: {self.location}")
            print(f"Время работы: {self.time}")

    class IceCreamStand(Restaurant):
        def __init__(self, name, kitchen, flavors, location, time):
            super().__init__(name, kitchen)
            self.flavors = flavors
            self.location = location
            self.time = time

        def spisok(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

        def availability(self):
            flavor = input("Введите вкус: ")
            if flavor in self.flavors:
                print("Вкус есть")
            else:
                print("Такого вкуса нет")

    iceCreamStand = IceCreamStand("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"], "Москва", "10:00-20:00")

    print(iceCreamStand.name)   #вызов атрибутов
    print(iceCreamStand.kitchen)
    print(iceCreamStand.location)
    print(iceCreamStand.time)

    iceCreamStand.describe_restaurant() #вызов методов

    iceCreamStand.spisok()
    iceCreamStand.availability()    #проверка наличия
print(z4())


def z5():
    input("Задача 2.4: подклассы")
    class Restaurant:
        def __init__(self, name, kitchen):
            self.name = name
            self.kitchen = kitchen

        def describe_restaurant(self):
            print(f"Ресторан: {self.name}")
            print(f"Кухня: {self.kitchen}")

    class IceCreamStand(Restaurant):
        def __init__(self, name, kitchen, flavors, location, time):
            super().__init__(name, kitchen)
            self.flavors = flavors
            self.location = location
            self.time = time

        def spisok(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    class Stick(IceCreamStand): #1й подкласс
        def __init__(self, name, kitchen, flavors, location, time, icename1, price):
            super().__init__(name, kitchen, flavors, location, time)
            self.icename1 = icename1
            self.price = price

        def about1(self):
            print(f"Название: {self.icename1}")
            print(f"Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)
            print(f"Цена: {self.price}")

    class Soft(IceCreamStand):  #2й подкласс
        def __init__(self, name, kitchen, flavors, location, time, icename2, flavor2, price):
            super().__init__(name, kitchen, flavors, location, time)
            self.icename2 = icename2
            self.flavor2 = flavor2
            self.price = price

        def about2(self):
            print(f"Название: {self.icename2}")
            print(f"Вкус: {self.flavor2}")
            print(f"Цена: {self.price}")

    iceCreamStand = IceCreamStand("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"], "Москва", "10:00-20:00")
    stick = Stick("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Фисташка"], "Москва", "10:00-20:00", "Мороженое на палочке", "30 руб")
    soft = Soft("Мороз", "Мороженое", ["Шоколад", "Ваниль", "Клубника", "Фисташка", "Карамель"], "Москва", "10:00-20:00", "Мягкое мороженое", "Пломбир", "100 руб")

    print(iceCreamStand.name)
    print(iceCreamStand.kitchen)
    iceCreamStand.describe_restaurant()
    iceCreamStand.spisok()

    stick.about1()
    soft.about2()
print(z5())