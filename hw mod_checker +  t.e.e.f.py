        #t.e.e.f.
    
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

        #mod_checker
        
def mod_checker(x, mod=0):
    return lambda z:True if z%x == mod else False
mod_3 = mod_checker(3)
print(mod_3(3))
