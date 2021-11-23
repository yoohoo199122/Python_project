my_list = [4, 2, 2, 1, 7, 3, 10, 10, 1, 7]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)