# Final Project for CS 102
# Restaurant Recommendation app

from restaurantData import types, restaurant_data

temp_dict = {}

for type in types:
    temp_dict[type] = []
    for restaurant in restaurant_data:
        if restaurant[0] == type:
            temp_dict[type].append({'name': restaurant[1],
                               'price': restaurant[2],
                               'rating': restaurant[3],
                               'address': restaurant[4]})

def greeting():
    print("#" * 37)
    print("\nWelcome to Restaurant Recommendations\n")
    print_food_types()
    print()

def get_user_input():
    response = ""
    while True:
        response = input("Type the food you would like to eat: ")
        if response.lower() in types:
            break
    return response.lower()

def print_food_types():
    response = ""
    while True:
        response = input("Would you like to see the food types? y/n?: ")
        if response.lower() == 'y':
            print()
            for type in types:
                if type == types[-1]:
                    print(type.capitalize())
                else:
                    print(f"{type.capitalize()}, ", end="")
            break
        else:
            return None

def print_results(response, restaurant_dict):
    print("\n")
    for restaurant in restaurant_dict[response]:
        print("#" * 25)
        print(restaurant['name'])
        print(f"Price: {restaurant['price']}/5")
        print(f"Rating: {restaurant['rating']}/5")
        print(restaurant['address'])
        print("#" * 25 + "\n")

def ask_again():
    response = ""
    while True:
        response = input("Would you like another recommendation? y/n: ")
        if response.lower() == 'y':
            return True
        else:
            return False

def main():
    greeting()
    response = get_user_input()
    print_results(response, temp_dict)
    if ask_again():
        main()

if __name__ == '__main__':
    main()