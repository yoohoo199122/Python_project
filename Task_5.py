def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number: list[str] = input('Введите число или букву j для прекращения подсчета - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'j' or number[el] == 'j':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма введеных цифр составляет: {sum_res}')
    print(f'Финальная сумма всех ранее введенных чисел равна: {sum_res}')


my_sum()
