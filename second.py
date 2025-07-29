### python in a program to do more things related to the world's 
### Name : Subin Thapa

#### Restuarant Management System: 
'''
 print("\n--- Restaurant Management System ---")
        print("1. Show Menu")
        print("2. Take New Order")
        print("3. Show All Orders")
        print("4. Search Order")
        print("5. Exit")

'''



menu = {
    "Burger": 50,
    "MoMo": 150,
    "Noodles": 899,
    "Fried Rice": 600
}

order  = []
### Function For Menu Section: 
def show_menu():
    print(" -- Menu-- ")
    for item in menu:
        print(f"{item}:Rs{menu[item]}")
### Function For taking order for the foods: : 

def take_order():
    
    

