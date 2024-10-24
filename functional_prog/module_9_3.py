first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1) - len(s2) 
                for s1, s2 in zip(first, second) 
                if len(s1) != len(s2) )

# second_result = (len(first[i]) - len(second[i])
#                  for i in range(min(len(first), len(second))))

second_result = (True if (len(first[i]) - len(second[i])) == 0 else False
                 for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
