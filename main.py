def get_data(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            ingredients_quantity = int(file.readline().strip())
            for ingredient in range(0, ingredients_quantity):
                types = file.readline().strip().split(' | ')
                types_dic = {}
                types_dic['ingredient_name'] = types[0]
                types_dic['quantity'] = types[1]
                types_dic['measure'] = types[2]
                cook_book[dish].append(types_dic)
            file.readline()
    return cook_book

# cook_book = get_data('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_data('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {}
                shop_list[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                shop_list[ingredient['ingredient_name']]['quantity'] = int(ingredient['quantity']) * person_count
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def sort_files_by_string(file_name_1, file_name_2, file_name_3):
    with open(file_name_1, encoding='utf-8') as file_1:
        with open(file_name_2, encoding='utf-8') as file_2:
            with open(file_name_3, encoding='utf-8') as file_3:
                sorted_length = ['','','']
                len_file_1 = len(file_1.readlines())
                len_file_2 = len(file_2.readlines())
                len_file_3 = len(file_3.readlines())
                if len_file_1 < len_file_2 and len_file_1 < len_file_3:
                    sorted_length[0] = file_name_1
                    if len_file_2 < len_file_3:
                        sorted_length[1] = file_name_2
                        sorted_length[2] = file_name_3
                    else:
                        sorted_length[1] = file_name_3
                        sorted_length[2] = file_name_2
                elif len_file_2 < len_file_3:
                    sorted_length[0] = file_name_2
                    if len_file_1 < len_file_3:
                        sorted_length[1] = file_name_1
                        sorted_length[2] = file_name_3
                    else:
                        sorted_length[1] = file_name_3
                        sorted_length[2] = file_name_1
                else:
                    sorted_length[0] = file_name_3
                    if len_file_1 < len_file_2:
                        sorted_length[1] = file_name_1
                        sorted_length[2] = file_name_2
                    else:
                        sorted_length[1] = file_name_2
                        sorted_length[2] = file_name_1
    with open('sortedtext.txt', 'w', encoding='utf-8') as new_file:
        with open(sorted_length[0], encoding='utf-8') as file_by_string_1:
            new_file.write(f'{sorted_length[0]}\n')
            new_file.write(f'{str(len(file_by_string_1.readlines()))}\n')
            file_by_string_1.seek(0)
            for line in file_by_string_1:
                new_file.write(line)
        with open(sorted_length[1], encoding='utf-8') as file_by_string_2:
            new_file.write(f'\n{sorted_length[1]}\n')
            new_file.write(f'{str(len(file_by_string_2.readlines()))}\n')
            file_by_string_2.seek(0)
            for line in file_by_string_2:
                new_file.write(line)
        with open(sorted_length[2], encoding='utf-8') as file_by_string_3:
            new_file.write(f'\n{sorted_length[2]}\n')
            new_file.write(f'{str(len(file_by_string_3.readlines()))}\n')
            file_by_string_3.seek(0)
            for line in file_by_string_3:
                new_file.write(line)

# sort_files_by_string('1.txt', '2.txt', '3.txt')