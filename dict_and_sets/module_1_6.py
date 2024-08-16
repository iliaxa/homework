my_dict = {'A': "Aзбука", 'b': ['boat', 'bear', 'beer'], 'C': 'Cловарь'}
print('Dict: ', my_dict)
print('Буква А: ', my_dict['A'])
my_dict['d'] = 4**4 
print('Value from New pair: ', my_dict['d'])  
my_dict.update({'e': 4*4,
                'f': 4+4})
b = my_dict.pop('b')
print('Value of deleted key: ', b)
print('Fresh dict: ', my_dict, '\n')

my_set = {3, 'ready', 2, 'steady', 2, 'go', True, 'ready', False}
print('Unic set: ', my_set)
# my_set.add('fire')
# my_set.add('shoot')
a = 'fire', 'shoot'
my_set.update(a)
my_set.discard(1) #1=True
print('fresh unic set: ', my_set)
