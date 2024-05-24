from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):

    dish_ingredients1 = set(dish_ingredients)
    return (dish_name, dish_ingredients1)

 
def check_drinks(drink_name, drink_ingredients):
    drink_ingredients_1 = set(drink_ingredients)
    ALCOHOLS_1 = set(ALCOHOLS)
    
    if drink_ingredients_1.intersection(ALCOHOLS_1)  == set():

        return (str(drink_name) + " " + "Mocktail")

    else:
        return (str(drink_name) + " " + "Cocktail")
