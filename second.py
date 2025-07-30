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
                continue 
            elif item in order_items:
                order_items[item] += qty_input
            else:
                order_items[item] = qty_input
            total = menu[item] * qty_input + total
        else:
            print("Invalid item. Please choose from the me")

        if len(order_items) > 0:
            order.append({
                "customer": customer_name,
                "items": order_items,
                "total": total
            })
            print(f" Order taken for {customer_name}. Total bill: Rs {total}")
        else:
            print("No items ordered.")


def show_all_order():
        if len(order) == 0:
            print(" No orders placed today.")
            return 
        print("--- All Orders ---")
        index = 1
        for i  in order:
            print(f"Order: {str(index)}")
            print(f"Customer Name: {i['customer']}")
            print("Items Ordered:")
            for item in i['items']:
                print(f"  {item}: {i['items'][item]} pcs")
            print(f"Total Bill: Rs {i['total']}")
            index += 1
def search_order():
    name = input("Enter customer name to search: ")
    for j in order:
        if j["customer"].lower() == name.lower():
            print(f" Order found for {j['customer']}")
            print("Items Ordered:")

            
            for item in j['items']:
                print(f"  {item}: {j['items'][item]} pcs")
            print(f"Total Bill: Rs {j['total']}")
            break
        else:
            print("No order found for that customer.")

#### For the main menu program 

def main():



    print("\n--- Restaurant Management System ---")
    print("1. Show Menu")
    print("2. Take New Order")
    print("3. Show All Orders")
    print("4. Search Order")
    print("5. Exit")

    while True:
      
        choice = input("Enter the choice between (1-4): ")
        if choice == "1":
            show_menu()
        elif choice == "2":
            take_order()
        elif choice == "3":
            show_all_order()
        elif choice == "4":
            search_order()
        elif choice == "5":
            print("Existing From the Restaurement Management Systems:  ")
            break
            
        else:
            print("Invalid Choice: Please Enter between (1-4): ")
main()


        
        
        
        

