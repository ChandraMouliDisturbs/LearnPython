# Author Chandra Mouli
input_list = ["1","2","3","4"]

def using_clause(in_list):
    out_list = list();
    [out_list.append(int(elem))for elem in in_list]
    return out_list

def using_map(in_list):
    return map(int, in_list)

print using_clause(input_list)
print sum(using_clause(input_list))
print using_map(input_list)
print sum(using_map(input_list))
print sum(input_list) #TypeError: unsupported operand type(s) for +: 'int' and 'str'