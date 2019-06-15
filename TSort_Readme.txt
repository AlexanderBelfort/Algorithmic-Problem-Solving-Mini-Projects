He made each turtle stand on another one's back and he piled them up in a nine-turtle stack. And then Yertle climbed up. He sat down on the pile. What a wonderful view! He could see 'most a mile!

The problem:

King Yertle wishes to rearrange his turtle throne to place his highest-ranking nobles and closest advisors nearer to the top. A single operation is available to change the order of turtles in the stack: a turtle can crawl out of its position in the stack and climb up over the other turtles to sit on the top.

Given an original ordering of a turtle stack and a required ordering for the same turtle stack, my job is to determine a minimal sequence of operations that rearranges the original stack into the required stack.

The first line of the input consists of a single integer K giving the number of test cases. 

Each test case consists of an integer n giving the number of turtles in the stack.

The next n lines specify the original ordering of the turtle stack. Each of the lines contains the name ofa turte, starting with the turtle on the top of the stack and working down to the turtle at the bottom of the stack. Turtles hae unique names, each of which is a string. The next n lines in hte input gives the desired ordering of the stack, once again by naming turtles from top to bottom. Each tes case consists exactly 2n+1 lines in total. The number of turtles (n) will be less than or equal to two hundred.

For each test case, the output consists of a single integer (one integer per line) indicating the minimum number of turtles that need to leave their position and crawl to the top in order to transform the original stack into the final stack.

In:
2
3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
9
Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixxon
Mr. Rogers
Ford perfect
Mack
Yertle
Richard M. Nixxon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack

Out:
1
3
