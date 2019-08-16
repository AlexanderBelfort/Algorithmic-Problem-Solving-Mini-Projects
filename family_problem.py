import sys
from statistics import median


def distance(list_houses):
    median_list = median(list_houses)
    counter = 0
    for item in range(len(list_houses)):
        counter += abs(list_houses[item] - median_list)
    return counter

def run():
    input_manual =  sys.stdin.readline()
    for item in range(int(input_manual)):
        input_manuall = sys.stdin.readline().split()
        input_manuall = [int(n) for n in input_manuall]
        print(int(distance(input_manuall[1:])))

run()