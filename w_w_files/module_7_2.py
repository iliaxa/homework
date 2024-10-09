def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    counter = 1
    for string in strings:
        byte_start = file.tell()
        file.write(string + '\n')
        _tuple = (counter, byte_start)
        strings_positions[_tuple] = string
        counter += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
