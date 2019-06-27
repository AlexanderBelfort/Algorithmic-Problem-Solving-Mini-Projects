import sys                                          #for the usage of STDIN and STDOUT

def adc(x, y):

    if x == 0 and y == 0:                           #last line of input will be 0 0
        sys.exit()




    z = lambda n: sum(map(int, str(n)))
    i = int((z(x) + z(y) - z(x + y)) / 9)           #internalizing the appropriate formula
    if i == 0:
        return print("No carry operation.")         #no carry operation for line of input
    elif i == 1:
        return print(str(i) + " carry operation.")  #carry operation for line of input
    else:
        return print(str(i) + " carry operations.")



def run():
    x, y = sys.stdin.readline().strip().split(" ")
    in_put = x, y                                   #initialize our inputs

    while in_put[0] != '0' and in_put[1] != '0':    #last line executor
        x = int(x)
        y = int(y)
        adc(x, y)
        x, y = sys.stdin.readline().strip().split(" ")
        in_put = x, y
