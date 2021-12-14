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
