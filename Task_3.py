a = int(input('Введите число месяца: '))
if a == 1 or a == 2 or a == 12:
    print ('Зима')
elif a == 3 or a == 4 or a == 5:
    print ('Весна')
elif a == 6 or a == 7 or a == 8:
    print ('Лето')
elif a == 9 or a == 10 or a == 11:
    print ('Осень')
else:
    print ('Ошибка ввода. Такого есяца не существует, введите от 1 до 12')