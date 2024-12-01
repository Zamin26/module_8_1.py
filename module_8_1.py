def add_everything_up(a, b):                # складывать числа(int, float) и строки(str)
    try:
        if type(a) != type(b):
            return format(a + b, ".3f")
    except TypeError:               # строковое представление двух данных
        return f'{a}' + f'{b}'






print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

