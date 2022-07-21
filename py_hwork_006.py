'''3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
*Пример:*
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"],           ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],    ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"],           ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"],                       ищем: "123", ответ: -1
- список: [],                                               ищем: "123", ответ: -1'''

listOne = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
listSecond = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
listThird = ["йцу", "фыв", "ячс", "цук", "йцукен"]
listFour = ["123", "234", 123, "567"]
listEmpty = []

numberOFList = int(input("Введите номер списка, из 5-ти возможных в котором будем искать значения:    "))
stringSearch = input("Введите текст для поиска второго вхождения в списке:  ")

def ListSearch (stringSearch, listNumber):
    entryString = "Нет второго вхождения"
    for i, string in enumerate(listNumber):
        if string == stringSearch and i > 1:
            entryString = (f"Элемент [{stringSearch}] находится в списке на {i} позиции")
            #print(f"{entryString} + {string}")
    return entryString


if numberOFList == 1: print(ListSearch (stringSearch, listOne))
elif numberOFList == 2: print(ListSearch (stringSearch, listSecond))
elif numberOFList == 3: print(ListSearch (stringSearch, listThird))
elif numberOFList == 4: print(ListSearch (stringSearch, listFour))
elif numberOFList == 5: print(ListSearch (stringSearch, listEmpty))