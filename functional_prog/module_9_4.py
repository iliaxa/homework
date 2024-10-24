from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words  
    def __call__(self):
        return choice(self.words)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                if isinstance(data, list):
                    # file.write(' '.join(map(str, data)) + '\n')
                    file.write(str(data) + '\n')
                    # for item in data:
                    #     file.write(str(item) + '\n')
                else:
                    file.write(data + '\n')
    return write_everything

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
     
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
