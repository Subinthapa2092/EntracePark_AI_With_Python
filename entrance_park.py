### Main used : For loop, while loop,dictionary and last  Function: 


##### Write a Program in a Python to do the restraunt Management System: 
#### Name: Subin Thapa 


### lists of the food in the dictionary 
menu = {
    "burger": 150,
    "pizza": 300,
    "fries": 100,
    "coke": 50,
    "momo": 120
}


### Empty for storing later all the data of each customers: For the Json data: 
orders  = [] 
#### function with showing menu : 
def show_menu():
    print("--- Menu ---")
    for item in menu: 
        print(f"{item}: Rs {menu[item]}")


### defining fuction for  the taking order
def take_order():
    customer_name = input("Enter customer name: ")
    order_items = {}
     ## empty dictionary  for stroing one's order data at a time: 
    total = 0
    show_menu()

    while True:
        item = input("Enter item  you want to order or type ('Done') : ").lower()
        if item == "done":
            break
        elif item in menu:
            qty_input = int(input(f"Enter quantity for {item}: "))
            if qty_input <= 0:
                print("Quantity must be greater than 0.")
                continue ### skip the things 
            elif item in order_items:
                order_items[item] += qty_input
            else:
                order_items[item] = qty_input
            total = menu[item] * qty_input + total
        else:
            print("Invalid item. Please choose from the me")

    if len(order_items) > 0:
        orders.append({
            "customer": customer_name,
            "items": order_items,
            "total": total
        })
        print(f"Order taken for {customer_name}. Total bill: Rs {total}")
    else:
        print("No items ordered.")
   ### Showing all orders in the form of the function: 

def show_all_orders():
    if len(orders) == 0:
        print(" No orders placed today.")
        return 
    print("--- All Orders ---")
    index = 1
    for i  in orders:
        print(f"Order: {str(index)}")
        print(f"Customer Name: {i['customer']}")
        print("Items Ordered:")
        for item in i['items']:
            print(f"  {item}: {i['items'][item]} pcs")
        print(f" Total Bill: Rs {i['total']}")
        index += 1

#### function with Search Order
def search_order():
    name = input("Enter customer name to search: ")
    found = False ## Assume No Matched Found : 
    for order in orders:
        if order["customer"].lower() == name.lower():
            print(f"\nOrder found for {order['customer']}")
            print("Items Ordered:")
            for item in order['items']:
                print(f"  {item}: {order['items'][item]} pcs")
            print(f"Total Bill: Rs {order['total']}")
            found = True
    if not found:
        print("No order found for that customer.")



##### Menu Whole  System: 
def main():
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Show Menu")
        print("2. Take New Order")
        print("3. Show All Orders")
        print("4. Search Order")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_menu()
        elif choice == 2:
            take_order()
        elif choice == 3:
            show_all_orders()
        elif choice == 4:
            search_order()
        elif choice == 5:
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

### Running the Program with  main function
main()
