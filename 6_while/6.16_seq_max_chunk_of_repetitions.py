# http://pythontutor.ru/lessons/while/problems/seq_max_chunk_of_repetitions/

n = int(input())
i, i_max = 1, 0
while n != 0:
    c = int(input())
    if c == n:
        i += 1
    else:
        if i > i_max:
            i_max = i
        i = 1
    n = c
print(i_max)