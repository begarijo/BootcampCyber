# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 18:00:47 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 13:51:23 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

Cookbook = {
    "Sandwich": {
    "Ingredients": ["tomatoe", "bread", "ham", "cheese"],
    "Meal": "Lunch",
    "Prep": 10
    },
    "Cake": {
    'Ingredients': ['Flour', 'Sugar', 'Eggs'],
    'Meal': 'Dessert',
    'Prep': 60
    },
    "Salad":  {
    'Ingredients': ['Avocado', 'Arugula', 'Tomatoes', 'Spinach'],
    'Meal': 'Lunch',
    'Prep': 15
    }
}
def print_name():
    print("The recipes are:")
    for name in Cookbook:
            print("- "+ name)

def print_recipe(name):
    if name in Cookbook:
        print("Recipe for {name}:\n-Ingredients: {Ingredients}\n-Meal: {Meal}\n-Prep time: {Prep}".format
              (name=name,
               Ingredients=Cookbook[name]["Ingredients"],
               Meal=Cookbook[name]["Meal"],
               Prep=Cookbook[name]["Prep"]))
    else:
        name = input("Does not exist baby, try another one;)")
        print_recipe(name)
    return

def del_recipe(name):
    if (name in Cookbook):
        del (Cookbook[name])
        print("Borrada:(")
    else:
        print("No existe amigui;)")
    return

def add_recipe():
    name = input("What's the name?\n")
    ingredients = input("Enter the ingredients:\n").split(', ')
    meal = input("When it's eaten?\n")
    prep = input("How much time do we need to prepare it?\n")
    Cookbook[name] = {
        "Ingredients": ingredients,
        "Meal": meal,
        "Prep": int(prep)
    }
    print_recipe(name)
    return

def menu():
    """docstring for menu"""
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the Cookbook")
    print("5: Quit")


def main():
    """docstring for main()"""
    print("Welcome to the Cookbook!:D")
    menu()
    try:
        while True:
            option = input("Choose an option:) que sea valido porfiplis\n")
            if (not option.isdigit()):
                continue
            option = int(option)
            if (option == 1):
                add_recipe()
            elif (option == 2):
                name = input("What recipe do you want to delete, so puta?")
                del_recipe(name)
            elif (option == 3):
                name = input("Which one?")
                print_recipe(name)
            elif (option == 4):
                print_name()
            elif (option == 5):
                print("Chao pescao!")
                break
    except:
        quit

if (__name__=='__main__'):
    main()
