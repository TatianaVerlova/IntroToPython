"(1+2)*3"

def parse(s):
    result = []
    digit = ''
    for symb in s:
        if symb.isdigit():
            digit += symb
        elif symb in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symb)
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symb)
    else:
        if digit:
            result.append(float(digit))
    return result

def calc(lst):
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

def brackets(lst):
    while '(' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]

print(parse("(1+2)*3"))