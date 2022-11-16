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