# Есть массив эл-тов, нужно найти неповторяющиеся элементы

lst = [1, 2, 3, 5, 1, 5, 3, 10]

def sort(lst):
    uniq_elements = set()
    for el in lst:
        if el not in uniq_elements:
            uniq_elements.add(el)
        else:
            uniq_elements.discard(el)
    s = list(uniq_elements)
    s.sort()
    return s