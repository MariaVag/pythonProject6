          # добавить обработку ValueError +

try:
    print(float('Что-то не то'))
except ValueError:
    print('ничего не получится, возникла ошибка "ValueError" ')
else:
    print('Всё хорошо')




      # добавить обработку FileNotFoundError, IOError

try:
    with open('myfile.txt', encoding='utf8') as file:
        a = file.readline()
        print(a)
except FileNotFoundError:
    print('ошибка "FileNotFoundError" файл не найден')
else:
    print('отличный файл')


try:
    a = open('myfile.txt')
    b = f.readline()
    c = int(s.strip())
    print(c)
except IOError:
    print('ничего не получится, возникла ошибка "IOError"')
else:
    print('всe получится')



         # добавить обработку ZeroDivisionError,+
a = 3
b = 0
try:
    res = a / b

    def divide_numbers(a, b):
        res = a/b
        return res

except ZeroDivisionError:
    print('ничего не получится, возникла ошибка "ZeroDivisionError"')



            # обработка TypeError+
try:
    a = 6
    b = 'Wow'
    res = a + b
except TypeError:
    print('возникает ошибка "TypeError"')
else:
    print('Успешно')


#  #          добавить обработку IndexError +
try:
    wow = ['a', 'b', '3']
    print(wow[5])
except IndexError:
    print('возникает ошибка "IndexError"')
else:
    print('успех')