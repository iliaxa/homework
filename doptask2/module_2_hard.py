first_plate = int(input('Введите число первой плиты: '))
second_plate = list(range(1,21))
second_plate_pass = []
for i in second_plate:
    for j in second_plate[i:len(second_plate)]:
        if first_plate % (i+j) == 0:
            second_plate_pass.append(i)
            second_plate_pass.append(j)
print('Пароль для второй плиты', second_plate_pass)
