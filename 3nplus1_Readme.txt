Consider an algorithm that takes in a number and processes it using the following rules:

If the number is 1, end;
If the number is odd, multiply by 3 and add 1;
If the number is even, divide by 2;

The algorithm repeats over this new number, until it ends (until the number is equal to 1)
Thus, for example, given the input number 22, the algorithm will yield the following sequence of numbers: 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

It is conjectured that this algorithm will terminate for any positive integer input value. However, nobody knows if this is actually the case.

Now given an input n, its cycle length is the length of the sequence of numbers obtained until 1 is reached. Therefore the cycle length of 22 is 16.

Your task is to determine the maximum cycle length over all numbers between a pair of integers.

INPUT: The program will be passed a pair of numbers into STDIN, one per line. The first number is the start of the sequence, the second is the end.
OUTPUT: Your program must print out on an individual line the maximum cycle length.

Example:
Input[0] = 1
Input[1] = 100
Output = 119