def create_dict_from_file(file_name):
    #""""""Функция чтения файла + создание словаря нужного формата""""""
    cook_dict = {}
    with open(file_name, encoding='utf-8') as file_work:
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