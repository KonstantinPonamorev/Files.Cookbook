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

data = get_data('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for dish in dishes:
        for ingredient in range(len(data[dish])):




get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'])
