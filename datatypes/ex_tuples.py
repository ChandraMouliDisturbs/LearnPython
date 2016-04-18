# Author Chandra Mouli
'''
Task
You are given an integer, NN, on a single line. The next line contains NN space-separated integers. Create a tuple, TT, of those NN integers, then compute and print the result of hash(TT).

Note: hash() is one of the functions in the __builtins__ module.

Input Format

The first line contains an integer, NN (the number of elements in the tuple).
The second line contains NN space-separated integers describing TT.
'''

N = int(raw_input())
content = raw_input().split(" ")
int_content = list()
[int_content.append(int(x)) for x in content]
print hash(tuple(int_content))

