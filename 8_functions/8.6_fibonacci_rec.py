# http://pythontutor.ru/lessons/functions/problems/fibonacci_rec/

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        q = fib(n - 2) + fib(n - 1)
        return q

print(fib(int(input())))