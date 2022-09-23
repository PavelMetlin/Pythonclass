day = int(input('введите номер : '))
if day > 7 or day < 1:
    print('введите номер')
elif day == 6 or day == 7:
    print("выходной!")
else:
    print("работай давай!")