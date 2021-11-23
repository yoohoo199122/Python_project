my_list = [4, 15, 9, 7, 2, 12, 10, 3, 14]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)