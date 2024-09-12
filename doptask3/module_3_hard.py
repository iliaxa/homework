def calculate_structure_sum(*args):
    structure_sum = 0
    for arg in args:
        if isinstance(arg, int):
            structure_sum += arg
        elif isinstance(arg, str):
            structure_sum += len(arg)
        elif isinstance(arg, dict):
            for i in arg.items():
                structure_sum += calculate_structure_sum(i)
        elif isinstance(arg, tuple):
            for i in arg:
                structure_sum += calculate_structure_sum(i)
        else:
            structure_sum += calculate_structure_sum(*arg)
        # print('elem-', arg, '\n summa=', structure_sum)
    return structure_sum



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
