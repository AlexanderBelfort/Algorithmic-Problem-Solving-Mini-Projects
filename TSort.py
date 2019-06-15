import sys                              #for the usage of STDIN and STDOUT

def t_sort(arrayone, arraytwo):         #intialize two arrays and a counter
    count = 0

    for i in range(len(arraytwo)):      #simple iterataion while initializing and
        if arrayone[0] == arraytwo[0]:  #initializing our stack data structure
            arrayone.pop(0)
            arraytwo.pop(0)
        else:
            arraytwo.pop(0)
            count += 1
    return count

def run():

    inputlists = []                     #store the inputs in this lsit

    outputlists = []                    #store the outputs in this list

    testnum = sys.stdin.readline()

    for cn in range(int(testnum)):
        turtles = sys.stdin.readline()  #initialize all of our turtles
        inputlist = []
        outputlist = []

        for ts in range(int(turtles)*2):
            if ts < int(turtles):
                input_line = sys.stdin.readline().strip()
                inputlist.append(input_line)
            else:
                output_line = sys.stdin.readline().strip()
                outputlist.append(output_line)

        inputlists.append(list(reversed(inputlist)))
        outputlists.append(list(reversed(outputlist)))

    for n in range(int(testnum)):
        print(t_sort(outputlists[n], inputlists[n]))