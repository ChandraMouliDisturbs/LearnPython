# Author Chandra Mouli
'''
You have a record of N students.
Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer N, the number of students.
The next N lines contains the name and marks obtained by that student separated by a space.
The final line contains the name of a particular student previously listed.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Constraints
2 <= N <= 10
0 <= Marks <= 100
'''
N = int(raw_input())
input_dict = {}
def get_average(student_name):
    if(input_dict.has_key(student_name)):
        lst = input_dict[student_name]
        lst = [float(x) for x in lst]
        print ("%.2f"%(sum(lst)/len(lst)))
for i in range(0,N):
    stu_details = raw_input()
    stu_list =  stu_details.split(" ")
    input_dict[stu_list[0]] = stu_list[1:]
stu_name_query = raw_input()
get_average(stu_name_query)
