# task 1

def task_1():
    nl=[]
    for x in range(1, 1000):
        if (x%3==0) and (x%5==0):
            nl.append(x)
    print (nl)

task_1()

#task 2

def task_2(s):
    d=l=0
    for c in s:
        if c.isdigit():
                d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    print('(', d, ', ', l, ')', sep='')

q = task_2("12abd3")

#task 3

def task_3(l1, l2):
    print(list(set(l1) - set(l2)), list(set(l2) - set(l1)))


task_3(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"])

#task 4

def task_4(L):
    x = int("".join(map(str, L))) #join убирает пробелы и запятые, а map преобразует числа в строки.
    print(x)

task_4([11, 44, 33])

#task 5

def task_5(num):
    print(max(num, key=sum))

task_5([[1,2], [3], [0, 12, 17, 6]])

#task 6

def task_6(n):
    r = 0
    if n > 0:
        while n > 0:
            digit = n % 10
            n //= 10
            r = r * 10 + digit
        print(r)
    if n < 0:
        n = str(n)
        c=len(n) # меряем строку
        v=n[c::-1] # срез
        print (v)  
task_6(2550)


# task 8

import math
def task_8(l):
    x = []
    q = 0
    for i in l:
        e = l[q]
        l.pop(q)
        c = math.prod(l)
        l.insert(0, e)
        x.append(c)
        
        q+=1
    print(x)
    return x
    
task_8([1, 2, 3, 4, 5])

