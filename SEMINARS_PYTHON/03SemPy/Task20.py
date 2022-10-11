# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']
num = int(input('Введите число: '))
num = str(num)
find_num = False
for string in list:
    if string.find(num) != -1:
        find_num = True
        break
if find_num:
    print('Это число содержится')
else:
    print('Этого числа нет')

# Вариант решения преподавателя, он проще:

# lst = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']
# num = int(input('Введите число для проверки: '))
# count = 0
# for elem in lst:
# if str(num) in elem:
# count += 1
# if count > 0:
# print ('Да, присутствует')
# else:
# print ('Не присутствует')