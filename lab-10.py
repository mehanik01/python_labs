import json

def z1():
    with open('123.json', 'r', encoding='utf-8') as f: # "r"- файл для чтения
        file1 = json.load(f) # загрузка содержимого файла в словарь

    for product in file1['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
z1()

def z2():
    with open('123.json', encoding='utf-8') as f:
        file2 = json.load(f)

    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Есть ли продукт в наличии?") == 'да' #значение "да" = true
    newspisok = {"name": name, "price": price, "available": available, "weight": weight}
    file2["products"].append(newspisok) #добавление словаря в начальный список

    with open('123.json', 'w', encoding='utf-8') as f:
        json.dump(file2, f)  #добавление нового списка в начальный файл

    print("Новый список:")
    with open('123.json') as f:
        data = json.load(f)
        for product in data['products']:
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']}")
            print(f"Вес: {product['weight']}")
            if product['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()
z2()

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        spisok = f.readlines() # сохранение всех строк файла в список

    ru_en = {} # словарь для русско-англа списка
    for line in spisok: # из каждой строки берем слово и его перевод
        engwords, ruswords = line.strip().split(' - ')
        for rusword in ruswords.split(','): # разбиваем русские слова на отдельные
            ru_en.setdefault(rusword.strip(), []).append(engwords.strip()) # "setdefault" добавляет новый слова в словарь

    sorted_dict = dict(sorted(ru_en.items())) # Сортировка по русским словам-ключам

    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word, en_words in sorted_dict.items():
            f.write(f"{ru_word} - {', '.join(en_words)}\n") # запись новых строк, "join" объединяет в строку, "\n"- новая строка
z3()