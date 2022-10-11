# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def second_in(list, find):
    count = 0
    for i in range(len(list)):
        if list[i] == find:
            count += 1
        if count == 2:
            return i
    return -1


list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
find = "йцу"

print(second_in(list, find))