from pprint import pprint
import os

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

def sort_file_by_string():
    directory = 'text/'
    texts_info = {}
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            text_params = []
            text_params.append(file)
            with open(f'{directory}{file}', encoding='utf-8') as f:
                text_params.append(f'{len(f.readlines())}')
                f.seek(0)
                text = []
                for line in f:
                    text.append(line)
                text_params.append(text)
            texts_info[f'{file}'] = text_params
        else:
            ...
    sorted_dict = sorted(texts_info.items(), key=lambda x: x[1][1])
    with open('sortedtext.txt', 'w', encoding='utf-8') as new_f:
        for text in sorted_dict:
            new_f.write(f'{text[1][0]}\n')
            new_f.write(f'{text[1][1]}\n')
            for line in text[1][2]:
                new_f.write(f'{line}')
            new_f.write(f'\n\n')

# sort_file_by_string()
