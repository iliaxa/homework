my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_len = len(my_list)
count = 0
while count < my_list_len and my_list[count] >= 0:
    if my_list[count] >0:
        print(my_list[count])
        count = count + 1
    else:
        count = count + 1
print('out of cycle')
