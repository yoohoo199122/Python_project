def my_func(a, b):
    try:
        z = a / b
        return z
    except ZeroDivisionError:
        z = 0
    except ValueError:
        return "вводите только число"


print(my_func(int(input("Введите число a:")), int(input("введите число b:"))))
