# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compr(string):
    compression = []
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        compression.append(count) 
        compression.append(str(string[i]))
        i += 1
    return compression

def decompr(compression):
    decompression = ""
    for i in range(0, len(compression), 2):
        decompression += compression[i] * compression[i + 1]
    return decompression

input_data = input("Введите данные, котрые необходимо сжать: ")
compressed_data = compr(input_data)
decompressed_data = decompr(compressed_data)
print(f"Сжатые данные:\n{compressed_data}\nВосстановленные данные:\n{decompressed_data}")