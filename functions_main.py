# functions for main program

from linked_list import LinkedList

def data_list(food_types, data):
    restaurant_data_list = LinkedList()
    for food_type in food_types:
        sublist = LinkedList()
        for restaurant in data:
            if restaurant[0] == food_type:
                sublist.insert(restaurant)
        restaurant_data_list.insert(sublist)
    return restaurant_data_list

def food_types(food_types):
    food_type_list = LinkedList()
    for type in food_types:
        food_type_list.insert(type)
    return food_type_list

def food_list(user_input, linked_food_list):
    type_list = []
    food_head = linked_food_list.get_head_node()
    while food_head.get_next_node() is not None:
        if food_head.get_value().startswith(user_input.lower()):
            type_list.append(food_head.get_value())
        food_head = food_head.get_next_node()
    return type_list

def print_foods(type_list, restaurants):
    all_restaurants = restaurants.get_head_node()
    while all_restaurants.get_next_node() is not None:
        current_restaurant = all_restaurants.get_value().get_head_node()
        if current_restaurant.get_value()[0] == type_list[0]:
            while current_restaurant.get_next_node() is not None:
                print("-" * 20)
                print(current_restaurant.get_value()[1])
                print("Price: " + "$" * int(current_restaurant.get_value()[2]))
                print("Rating: " + "*" * int(current_restaurant.get_value()[3]))
                print(current_restaurant.get_value()[4])
                current_restaurant = current_restaurant.get_next_node()
        all_restaurants = all_restaurants.get_next_node()
    return None

def greeting():
    print("""
    

                                                   
,------. ,------. ,---. ,--------. ,---.           
|  .--. '|  .---''   .-''--.  .--'/  O  \          
|  '--'.'|  `--, `.  `-.   |  |  |  .-.  |         
|  |\  \ |  `---..-'    |  |  |  |  | |  |         
`--' '--'`------'`-----'   `--'  `--' `--'         
,--. ,--.,------.   ,---.  ,--.  ,--.,--------.    
|  | |  ||  .--. ' /  O  \ |  ,'.|  |'--.  .--'    
|  | |  ||  '--'.'|  .-.  ||  |' '  |   |  |       
'  '-'  '|  |\  \ |  | |  ||  | `   |   |  |       
 `-----' `--' '--'`--' `--'`--'  `--'   `--'       
       ,------. ,------. ,-----. ,-----.           
,-----.|  .--. '|  .---''  .--./'  .-.  '          
'-----'|  '--'.'|  `--, |  |    |  | |  |          
       |  |\  \ |  `---.'  '--'\'  '-'  '          
       `--' '--'`------' `-----' `-----'           
,--.   ,--.,--.   ,--.,------.,--.  ,--.,------.   
|   `.'   ||   `.'   ||  .---'|  ,'.|  ||  .-.  \  
|  |'.'|  ||  |'.'|  ||  `--, |  |' '  ||  |  \  : 
|  |   |  ||  |   |  ||  `---.|  | `   ||  '--'  / 
`--'   `--'`--'   `--'`------'`--'  `--'`-------'  
,------.,------. ,------. ,------. ,------.        
|  .---'|  .--. '|  .--. '|  .--. '|  .--. '       
|  `--, |  '--'.'|  '--'.'|  '--'.'|  '--'.'       
|  `---.|  |\  \ |  |\  \ |  |\  \ |  |\  \        
`------'`--' '--'`--' '--'`--' '--'`--' '--'       
                                                   


    """)
    return None

def prompt_user():
    print("Enter a food type or the first letters of a food type: \n")
    return None

def goodbye():
    print("\nThanks for using Restaurant Recommenderrrr!")
    return None