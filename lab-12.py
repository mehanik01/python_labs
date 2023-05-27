import tkinter as tk

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("У нас есть такие разновидности мороженного:")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_ice_cream_stand = IceCreamStand("Сладкие угощения", "Кафе-мороженное", [input("введите вкус:"),input("введите вкус:"), input("введите вкус:")])
my_ice_cream_stand.show_flavors()

print()

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors, location, hours):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.hours = hours

    def show_flavors(self):
        print("У нас есть такие разновидности мороженного:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def show_hours(self):
        print("Кафе открыто:")
        for hours in self.hours:
            print(f" {hours}")

    def show_location(self):
        print("Кафе находится:")
        for location in self.location:
            print(f" {location}")

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"{new_flavor} был добавлен(а)!")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"{flavor} был(а) удален!")
        else:
            print(f"{flavor} нет в меню.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Да, у нас есть {flavor}!")
        else:
            print(f"Извините, у нас нет {flavor}.")

    def show_menu(self, menu_type):
        if menu_type == "пл":
            print("У нас есть следующие вкусы мороженого на палочке:")
            for flavor in [input("введите вкус:"),input("введите вкус:"), input("введите вкус:")]:
                print(f"- {flavor}")
        elif menu_type == "мм":
            print("У нас есть следующие вкусы мягкого мороженного:")
            for flavor in [input("введите вкус:"),input("введите вкус:"), input("введите вкус:")]:
                print(f"- {flavor}")
        elif menu_type == "хл":
            print("У нас есть следующие вкусы холодного льда:")
            for sundae in [input("введите вкус:"),input("введите вкус:"), input("введите вкус:")]:
                print(f"- {sundae}")
        else:
            print("Такого типа  нет")

my_ice_cream_stand = IceCreamStand("Сладкие угощения", "кафе-мороженое", [input("введите вкус:"),input("введите вкус:"), input("введите вкус:")], ["Большая морская"], ["10:00–22:00"])

my_ice_cream_stand.add_flavor(input("какой вкус добавить - "))
print()
my_ice_cream_stand.show_flavors()
print()
my_ice_cream_stand.remove_flavor(input("удалить вкус -"))
my_ice_cream_stand.check_flavor(input("проверить вкус -"))
my_ice_cream_stand.show_menu(input("проверить тип - "))
print()
my_ice_cream_stand.show_hours()
print()
my_ice_cream_stand.show_location()

class IceCreamStand:
    def __init__(self, root):
        self.root = root
        self.root.title('Ice Cream Stand')
        self.root.geometry('600x500')


        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(pady=20)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(pady=20)

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(pady=20)

        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(pady=20)


        self.label1 = tk.Label(self.frame1, text='Выберете топик:')
        self.label1.pack()

        self.var1 = tk.IntVar()
        self.checkbutton1 = tk.Checkbutton(self.frame2, text='Ананас', variable=self.var1)
        self.checkbutton1.pack()

        self.var2 = tk.IntVar()
        self.checkbutton2 = tk.Checkbutton(self.frame2, text='Шоколад', variable=self.var2)
        self.checkbutton2.pack()

        self.var3 = tk.IntVar()
        self.checkbutton3 = tk.Checkbutton(self.frame2, text='Карамель', variable=self.var3)
        self.checkbutton3.pack()

        self.var4 = tk.IntVar()
        self.checkbutton4 = tk.Checkbutton(self.frame2, text='Орехи', variable=self.var4)
        self.checkbutton4.pack()

        self.label2 = tk.Label(self.frame3, text='Выберете мороженное:')
        self.label2.pack()

        self.var5 = tk.StringVar()
        self.radio1 = tk.Radiobutton(self.frame4, text='Ванильное', variable=self.var5, value='Ванильное')
        self.radio1.pack()

        self.radio2 = tk.Radiobutton(self.frame4, text='Шоколадное', variable=self.var5, value='Шоколадное')
        self.radio2.pack()

        self.radio3 = tk.Radiobutton(self.frame4, text='Клубничное', variable=self.var5, value='Клубничное')
        self.radio3.pack()

        self.button = tk.Button(self.root, text='Выбрать', command=self.submit)
        self.button.pack(pady=20)

        self.output_label = tk.Label(self.root, text='')
        self.output_label.pack()

    def submit(self):

        toppings = []
        if self.var1.get() == 1:
            toppings.append('Ананасом')
        if self.var2.get() == 1:
            toppings.append('Шоколадом')
        if self.var3.get() == 1:
            toppings.append('Карамелью')
        if self.var4.get() == 1:
            toppings.append('Орехами')

        flavor = self.var5.get()


        if flavor and toppings:
            self.output_label.configure(text=f'Вы выбрали {flavor} мороженое с {", ".join(toppings)}!')
        else:
            self.output_label.configure(text='Пожалуйста выберете топик и шоколад')


root = tk.Tk()
app = IceCreamStand(root)
root.mainloop()
