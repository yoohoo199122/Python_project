my_str = input("Введите строку из нескольких слов: ")
a = my_str.split(" ")
for i, r in enumerate(a, 1):
    if len(r) > 10:
        r = r[0:10]
    print(f"{i}, - {r}")