try:
    f = int(input('Введите ЧИСЛО!!!'))
    a = int(input('Второе ЧИСЛО!!!'))
    print(f / a)
except ValueError:
        print('Сказал же ЧИСЛО!!!')
except ZeroDivisionError:
        print('IQ как у хлебуска?')
else:
        print('Всё хорошо.')
finally:
        print('Конец.')
