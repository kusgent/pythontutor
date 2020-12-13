# http://pythontutor.ru/lessons/functions/problems/reverse_rec/

def func():
    n = int(input())
    if n == 0:
        print(n)
    else:
        func()
        print(n)

func()