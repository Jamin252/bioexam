import copy
a = [0, 1]
x = a
x[0] = 2
print(x,a)
a = [0, 1]
x = copy.deepcopy(a)
x[0] = 2
print(x, a)