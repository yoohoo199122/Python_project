rus = {'one' : 'Один', 'two' : 'Два', 'three' : 'Три', 'four' : 'Четыре'}
new_file = []
with open('text_3.txt', 'r') as file_obj:
    #content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_3.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)