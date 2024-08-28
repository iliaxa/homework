def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['first', 52, False]
values_dict = {'a': 'second', 'b': True, 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['mem', ['ne', 'mem']]
print_params(*values_list_2)
print_params(*values_list_2, 42)
