# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки
# в другой.

string_1 = input("Введите первую строку: ")
string_2 = input("Введите вторую строку: ")
#print (string_1.count(string_2))

count = 0
for i in range(0, len(string_1) - len(string_2), 1):
    if string_2 in string_1[i:i+len(string_2)]:
        count += 1
        string_1 = string_1[i+len(string_2) + 1:]
    else:
        k = 1
print(count)