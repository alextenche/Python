
template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(values):
    result = []
    for value in values:
        result.append(template.format(**value))
    return result

values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

print(string_factory(values))
