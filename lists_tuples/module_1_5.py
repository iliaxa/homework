immutable_var = (1, True, 3, 'string', [4, 5], 6, 7)
print(' Тип: ', type(immutable_var), '\n',  immutable_var)
#immutable_var[2] = 10     # нельзя, потому что нельзя, блин. кортеж — неизменяемый тип данных
#immutable_var[4][1] = 'mojno'  #
mutable_list = [1, 2, 3, 'string', immutable_var, 6, False]
mutable_list[3] = 1.1
mutable_list[4][4][1] = 'mojno'
print(' Тип: ', type(mutable_list), '\n',  mutable_list)


#print(' Тип: ', type(immutable_var), id(immutable_var), '\n',  immutable_var)
# mutable_list.remove(immutable_var)
# print(' Тип: ', type(mutable_list), id(mutable_list), '\n',  mutable_list)
# mutable_list.remove(mutable_list[3])
# mutable_list.remove(mutable_list[2])
# print(' Тип: ', type(mutable_list), id(mutable_list), '\n',  mutable_list)
#print(immutable_var in mutable_list)
