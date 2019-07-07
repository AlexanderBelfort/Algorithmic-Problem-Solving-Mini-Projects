import sys                                      #for the usage of STDIN and STDOUT

#my aim is to implement the task
#the fastest way possible execution-wise
#the code should take no more than 3 seconds
#to run for input paramets 1 100000

def sequence(x, cache):                         #to achieve this we will use caching
    if x in cache:                              #and we will implement our formula recurisvely
        return cache[x]
    if x % 2 == 0:
        cycle = sequence(x//2, cache)
    else:
        cycle = sequence(3*x + 1, cache)
    cache[x] = cycle + 1
    return cache[x]

def cycle(a, b, cache):
    return max(sequence(i, cache) for i in range(a, b+1))

def run():
    cache = {1: 1}
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    a, b = min(a, b), max(a, b)
    m = cycle(a, b, cache)
    print(m)