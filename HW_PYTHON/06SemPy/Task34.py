# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий 
# сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0

def read_file(name):
    path = str(name)
    data = open(path, 'r')
    for line in data:
        pass
    data.close()
    return str(line)

file1 = read_file('Task33_1.txt')
file2 = read_file('Task33_2.txt')

print(file1)
print(file2)

def degrees_list(polynomial):
    # degrees = []
    # for i in polynomial:
    #     if i.isdigit():
    #         degrees.append(i)
    degrees = [i for i in polynomial if i.isdigit()] # применен LC
    return degrees

degrees_1 = degrees_list(file1)
degrees_2 = degrees_list(file2)

def degrees_summ(x,y):
    lst = [1,2,3,4,5,6,7]
    i = 0
    while i != len(x):
        lst[i] = int(x[i])+int(y[i])
        i+=1
    lst[1]=lst[1]//2
    lst[3]=lst[3]//2
    return lst

bc = degrees_summ(degrees_1, degrees_2)
summ_polynomial = f"{bc[0]}x^{bc[1]} + {bc[2]}x^{bc[3]} + {bc[4]}x + {bc[5]} = {bc[6]}"

with open(f"file_summ.txt","w") as data:
    data.write(summ_polynomial)

print("Сумма двух многочленов")
print(summ_polynomial)