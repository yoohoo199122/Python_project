subj = {}
with open('text_5.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = (lecture) + (practice) + (lab)
    print(f'Общее количество часов по предмету - \n {subj}')