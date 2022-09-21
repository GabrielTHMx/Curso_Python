from pathlib import *
from os import system


def starting_recipe():
    print("\t\t\tRECIPE MANAGER\n")
    name = input('Enter your name: ')
    system("cls")

    print("\t\tRECIPE MANAGER\n")
    print(f"\t\tWelcome {name.upper()} !")
    rute = Path("C:/Users/Gabriel/Documents/Pruebas/RECETAS")
    rute_windows = PureWindowsPath(rute)
    print(f"\n\tYour recipes are in:\n\t\t{rute_windows}")


def getting_recipes():
    rute = Path("C:/Users/Gabriel/Documents/Pruebas/RECETAS")
    my_list = list(rute.glob('**/*.txt'))
    # print(my_list)
    print("\n\tYour recipes are:\n")
    for number, r in enumerate(my_list):
        print('\t', number + 1, ".- ", r.stem)


def getting_directories():
    rute = Path("C:/Users/Gabriel/Documents/Pruebas/RECETAS")
    my_dirs = [x for x in rute.iterdir() if x.is_dir()]
    categories_f = 0
    print("\n\tYour categories are:\n")
    for number, r in enumerate(my_dirs):
        print('\t', number + 1, ".- ", r.stem)
        categories_f += 1
    return categories_f, my_dirs


def displaying_menu():
    print("\n\t\t\tMENU\n")
    print("""        [1] Reading recipe
        [2] Creating recipe
        [3] Creating category
        [4] Eliminating recipe
        [5] Eliminating category
        [6] Ending program\n""")
    option_f = int(input("\tWhat do yo want to do? Enter option: "))
    system("cls")
    return option_f


def selecting_category():
    return int(input("\n\t\tEnter a number of category: "))


def menu(option_f):
    star_f = 1
    rute = Path("C:/Users/Gabriel/Documents/Pruebas/RECETAS")
    if 0 < option_f <= 6:

        match option_f:
            case 1:
                system('cls')
                print("\t\tREADING RECIPE")
                reading_recipe()
                star_f = 1

            case 2:
                system('cls')
                print("\t\tCRATING RECIPE")
                creating_recipe()
                star_f = 1

            case 3:
                system('cls')
                print("\t\tCREATING CATEGORY")
                creating_category(rute)
                star_f = 1

            case 4:
                system('cls')
                print("\t\tELIMINATING RECIPE")
                eliminating_recipes()
                star_f = 1

            case 5:
                system('cls')
                print("\t\tELIMINATING CATEGORY")
                eliminating_category(rute)
                star_f = 1

            case 6:
                system('cls')
                print("\t\tENDING PROGRAM........")
                star_f = 0
    else:
        system('cls')
        print("\n\t\t\tINCORRECT OPTION. TRY AGAIN :)\n")
    return star_f


def opening_recipes(rute_or, my_list_or):
    recipe_or = int(input("\n\t\tEnter a number of recipe: "))
    system("cls")
    file = rute_or / my_list_or[recipe_or - 1]
    my_file = open(file)
    print(my_file.read())
    input("\n\tPress any key to continue....")
    my_file.close()


def showing_recipes(my_list2):
    print("\n\t\tYour recipes are:\n")
    for number, r in enumerate(my_list2):
        print('\t', number + 1, ".- ", r.stem)


def menu_categories(option_f, categories_f, directories_f):

    if 0 < option_f <= categories_f:
        rute_mc = directories_f[option_f - 1]
        my_list2 = list(rute_mc.glob('**/*.txt'))
        category_name = rute_mc.stem

        print(f"\n\t\t{category_name.upper()} CATEGORY")
        return my_list2, rute_mc


def reading_recipe():
    categories, directories = getting_directories()
    option_f = selecting_category()
    system('cls')
    # print(categories)
    my_list, rute_rc = menu_categories(option_f, categories, directories)

    if len(my_list) > 0:
        showing_recipes(my_list)
        opening_recipes(rute_rc, my_list)
    else:
        print("\n\t\tYou don´t have recipes. Add a new one :)\n")
        input("\n\tPress any key to continue....")


def creating_recipe():
    categories_cr, directories_cr = getting_directories()
    option_cr = selecting_category()
    system('cls')
    my_list_cr, rute_cr = menu_categories(option_cr, categories_cr, directories_cr)
    # print(rute_cr)
    name_recipe = input("\tEnter the name of your new recipe: ")
    file_recipe = name_recipe + '.txt'
    new_recipe = rute_cr / file_recipe
    my_file = open(new_recipe, 'w')
    my_file.close()
    print("\n\t\tEnter the new content:\n")
    my_file = open(new_recipe, 'a')
    line = input("\t Line 1:")
    my_file.write(line)
    my_file.close()
    print(f"\n\t\tRecipe {name_recipe} created correctly! ")
    print(f"\t\tRute: {PureWindowsPath(new_recipe)}")
    input("Press any key to continue....")
    system('cls')


def creating_category(rute_f):
    # print(rute_f)
    name_category = input("\n\tEnter name of new category: ")
    new_category = rute_f / name_category.upper()
    new_category.mkdir(parents=True, exist_ok=True)
    # print(new_category)
    input("Press any key to continue....")
    system('cls')


def eliminating_recipes():
    categories, directories = getting_directories()
    option_f = selecting_category()
    system('cls')
    my_list, rute_rc = menu_categories(option_f, categories, directories)
    # showing_recipes(my_list)
    # print(my_list)
    if len(my_list) > 0:
        showing_recipes(my_list)
        name_recipe = input("\n\tWhat recipe you wanna eliminate?. Enter name: ") + '.txt'
        recipe_path = rute_rc / name_recipe
        if recipe_path.exists():
            recipe_path.unlink()
            print(f"\n\t\tRecipe {name_recipe} eliminated")
            # print(rute_rc)
            # print(recipe_path)
        else:
            print("This file does not exists. Try again :)")
    else:
        print("\n\t\tYou don´t have recipes. Add a new one :)\n")
    input("Press any key to continue....")
    system('cls')


def eliminating_category(rute_f):
    categories, directories = getting_directories()
    # print(directories)
    if categories > 0:
        name_category = input("\n\tWhat category you wanna eliminate? Enter name: ")
        category = rute_f / name_category.upper()
        if category.exists():
            category.rmdir()
            print(f"\n\tCategory '{name_category}' eliminated")
        else:
            print("\n\tThis directory does not exists. Try again :)")
    else:
        print("\n\tYou don't have categories. Add a new one :)")

    input("\n\tPress any key to continue....")
    system('cls')


starting_recipe()
getting_recipes()
# option = displaying_menu()
start = 1
while start == 1:

    option = displaying_menu()
    start = menu(option)
    system('cls')
