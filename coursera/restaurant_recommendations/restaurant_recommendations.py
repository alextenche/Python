FILENAME = 'restaurants_small.txt'


def recomend(file, price, cuisine_list):
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    names_matching_price = price_to_names[price]

    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisine_list)


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisine_list):
    pass


def read_restaurants(file):
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    with open(file, 'r') as f:
        reviews = f.read().strip()
        restaurants = [entry.split('\n') for entry in reviews.split('\n\n')]

    for name, rating, price, cuisine in restaurants:
        name_to_rating[name] = rating
        price_to_names[price].append(name)
        name_cuisine = [name, cuisine.split(',')]

        for item in name_cuisine[1]:
            if item in cuisine_to_names.keys():
                cuisine_to_names[item].append(name_cuisine[0])
            else:
                cuisine_to_names[item] = [name_cuisine[0]]

    return name_to_rating, price_to_names, cuisine_to_names
