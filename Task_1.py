my_int = 7
my_float = 7.7
my_str = "Hello world"
my_list = ['a', '7']
my_tuple = ('b', '5')
my_dict = {'car': 'lambo', 'ball': 'Yellow'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')