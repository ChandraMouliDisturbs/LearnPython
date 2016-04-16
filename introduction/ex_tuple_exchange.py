a = raw_input()
b = raw_input()
tup = (a,b)
tup = tuple(reversed(tup))
for element in tup:
    print element