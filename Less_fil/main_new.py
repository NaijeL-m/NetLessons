def create_dict_from_file(file_name):
    #""""""Функция чтения файла + создание словаря нужного формата""""""
    cook_dict = {}
    with open(file_name, encoding='UTF-8') as file_work:
        for line in file_work:
            dish_name = ''
            print(line.lower().strip())
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                print(file_work.readline().lower())
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            file_work.readline()
    return cook_dict
print(create_dict_from_file('recipes.txt'))



#Zadacha 3 new
def create_ans(a,way,name_ans):
    sort = []
    sort_ind = []
    sortOut = ['0' for i in a]
    for i in a:
        with open(way + i, 'r', encoding='UTF-8') as f:
            ff = f.readlines()
            ff.append(i)
            sort_ind.append(len(ff))
            sort.append(ff)
    sort_ind = sorted(sort_ind)
    for i in range(len(sort_ind)):
        for j in sort:
            if sort_ind[i] == len(j):
                sortOut[i] = j
    f = open(name_ans, 'w', encoding='UTF-8')
    for i in sortOut:
        f.write('\n' + i[-1] + '\n')
        f.write(str(len(i) - 1) + ' стр.' + '\n')
        for j in i[:-1]:
            f.write(j)
    f.close()
create_ans(['1.txt','2.txt','3.txt'],'SORTed/','Ответы.txt')