my_dict = {'a': "азбука", 'b': ['boat', 'bear', 'beer'], 'c': 'словарь'}
print(my_dict['a'])
my_dict['d'] = 4**4 
print(my_dict['d'])  
my_dict.update({'e': 4*4,
                'f': 4+4})
b = my_dict.pop('b')
print(b)
print(my_dict)

my_set = {3, 'ready', 2, 'steady', 2, 'go', True, 'ready', False}
print('\n', my_set)
# my_set.add('fire')
# my_set.add('shoot')
a = 'fire', 'shoot'
my_set.update(a)
my_set.discard(1) #1=True
print(my_set)
