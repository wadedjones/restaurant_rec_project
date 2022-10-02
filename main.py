# Final Project for CS 102
# Restaurant Recommendation app

from restaurantData import types, restaurant_data
from functions_main import *

restaurants = data_list(types, restaurant_data)
foods = food_types(types)

def main():
    greeting()
    prompt_user()
    while True:
        user_input = input()
        matching_foods = food_list(user_input, foods)
        if len(matching_foods) == 1:
            response = input(f"\nWould you like to see {matching_foods[0]} restaurants? y/n: ").lower()
            if response == 'y':
                print("\n")
                print_foods(matching_foods, restaurants)
                ask_again = input("\nWould you like more recommendations? y/n: \n")
                if ask_again == 'y':
                    prompt_user()
                    continue
                else:
                    goodbye()
                    break
            else:
                prompt_user()
                continue
        elif len(matching_foods) > 1:
            print(f"We have multiple food types that start with '{user_input}', including: \n")
            for food in matching_foods:
                print(food)
            print("Enter the food you would like data on: \n")
            continue
        else:
            print(f"Sorry. We don't have data on food types that start with '{user_input}'")
            response_2 = input("Would you like to enter a different food type? y/n: \n").lower()
            if response_2 == 'y':
                continue
            else:
                goodbye()
                break

if __name__ == '__main__':
    main()