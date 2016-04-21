# Author Chandra Mouli

'''
Lists functions
1.) append(x)
2.) insert(i,x)
3.) remove(x)
4.) pop()
5.) index(x)
6.) count(x)
7.) sort()
8.) reverse()
Task
Initialize your list (L = []) and follow the N commands given over N lines.

Each command will be 1 of the 8 commands given above. Each command will have its own value(s) separated by a space.

Input Format

The first line contains an integer, N (the number of commands).
The NN subsequent lines each contain one of the 88 commands described above.

Sample input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
central_list = list()
exec_map = list()

def execute_sequence():
    list_cmd = "central_list."
    for li in exec_map:
        command_name = li[0].lower()
        if(len(li)==1):
            if (command_name=="print"):
                print central_list
            else:
                central_list.__getattribute__(command_name).__call__()
                # exec(list_cmd+command_name+"()")
        elif(len(li)==2):
                single_param = li[-1]
                central_list.__getattribute__(command_name).__call__(single_param)
        else:
            param1 = li[1]
            param2 = li[-1]
            central_list.__getattribute__(command_name).__call__(int(param1), int(param2))

N = int(raw_input())
for i in range(N):
    exec_map.append(raw_input().split(" "))
execute_sequence()
