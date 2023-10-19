# zomato_chronicles.py
import json
import os

# Import the required libraries
from tabulate import tabulate
from colorama import Fore, Back, Style

# Define file names
menu_file = "menu.json"
snacks_file = "snacks.json"
orders_file = "orders.json"

# Function to load data from JSON files or initialize with an empty list
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Function to save data to JSON files
def save_data_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Load menu, snacks, and orders data
menu = load_data(menu_file)
snacks = load_data(snacks_file)
orders = load_data(orders_file)

# Function to update order status
def update_order_status(order_id, new_status):
    for order in orders:
        if order.get("order_id") == order_id:
            order["status"] = new_status
            save_data_to_json(orders, orders_file)
            break

# Function to display the menu
def display_menu():
    if not menu:
        print("The menu is empty.")
        return
    # Create a list of lists for tabulate
    table = []
    for dish in menu:
        table.append([dish['dish_id'], dish['dish_name'], f"${dish['price']}", dish['availability']])

    # Define table headers
    headers = ["Dish ID", "Dish Name", "Price", "Availability"]

    # Print the formatted table with colored text
    print(Fore.CYAN + tabulate(table, headers, tablefmt="grid"))
    print(Fore.RESET)

# Function to display snacks
def display_snacks():
    if not snacks:
        print("There are no snacks available.")
        return
    # Create a list of lists for tabulate
    table = []
    for snack in snacks:
        table.append([snack.get('snack_id', ''), snack.get('snack_name', ''), f"${snack.get('price', 0)}", snack.get('quantity', '')])

    # Define table headers
    headers = ["Snack ID", "Snack Name", "Price", "Quantity"]

    # Print the formatted table with colored text
    print(Fore.GREEN + tabulate(table, headers, tablefmt="grid"))
    print(Fore.RESET)

# Define possible order statuses
order_statuses = ["received", "preparing", "ready for pickup", "delivered"]

# Function to take a new order
def take_new_order():
    customer_name = input("Enter Customer Name: ")

    print("Do you want to add snacks to the order? (yes/no): ")
    add_snacks = input().strip().lower() == "yes"
    ordered_snacks = []
    if add_snacks:
        if not snacks:
            print("There are no snacks available to add to the order.")
            return
        print(Fore.GREEN +"Available Snacks:")
        display_snacks()
        ordered_snacks = [int(x) for x in input("Enter Snack IDs (comma-separated): ").split(",")]

    print("Do you want to add dishes to the order? (yes/no): ")
    add_dishes = input().strip().lower() == "yes"
    ordered_dishes = []
    if add_dishes:
        if not menu:
            print("The menu is empty. There are no dishes available to add to the order.")
            return
        print(Fore.GREEN +"Available Dishes:")
        display_menu()
        ordered_dishes = [int(x) for x in input("Enter Dish IDs (comma-separated): ").split(",")]

    if not ordered_snacks and not ordered_dishes:
        print("You must select at least one snack or dish to place an order.")
        return

    new_order_id = max([order.get("order_id", 0) for order in orders], default=0) + 1
    order_status = "received"
    new_order = {"order_id": new_order_id, "customer_name": customer_name, "snacks": ordered_snacks, "dishes": ordered_dishes, "status": order_status}
    orders.append(new_order)
    save_data_to_json(orders, orders_file)
    print(Fore.GREEN +"Order taken successfully. Enjoy your meal! 🍔")
    print(Fore.RESET)

# Function to display orders
def display_orders():
    if not orders:
        print("There are no customer orders.")
        return

    print("\nCustomer Orders:")
    for order in orders:
        order_id = order.get("order_id")
        customer_name = order.get("customer_name")
        snack_ids = order.get("snacks", [])
        dish_ids = order.get("dishes", [])
        order_status = order.get("status")

        snacks_str = ", ".join([snack["snack_name"] for snack in snacks if snack["snack_id"] in snack_ids])
        dishes_str = ", ".join([dish["dish_name"] for dish in menu if dish["dish_id"] in dish_ids])

        print(f"Order ID: {order_id}, Customer Name: {customer_name}")
        if snacks_str:
            print(f"Snacks: {snacks_str}")
        if dishes_str:
            print(f"Dishes: {dishes_str}")
        print(f"Status: {order_status}")
        print("-" * 20)

# Function to filter orders by status
def filter_orders_by_status():
    filter_status = input("Enter Order Status to filter (received/preparing/ready for pickup/delivered): ")
    filtered_orders = [order for order in orders if order["status"] == filter_status]

    if not filtered_orders:
        print(f"No orders found with status '{filter_status}'.")
    else:
        print(f"\nOrders with Status '{filter_status}':")
        for order in filtered_orders:
            print(f"Order ID: {order['order_id']}, Customer Name: {order['customer_name']}, Status: {order['status']}")

# Inside the main program loop

def delete_order(order_id):
    global orders
    orders = [order for order in orders if order["order_id"] != order_id]
    save_data_to_json(orders, orders_file)


# Main program loop
while True:
    print("\n*** Zomato Chronicles: The Great Food Fiasco ***")
    print("1. Add a Dish to the Menu 🍕")
    print("2. Remove a Dish from the Menu 🚮")
    print("3. Add a Delicious Snack 🍟")
    print("4. Take a New Order 🍔")
    print("5. Update Order Status 🚚")
    print("6. View the Scrumptious Menu 📜")
    print("7. View Tasty Snacks 🍿")
    print("8. View Hungry Customer Orders 📦")
    print("9. Filter Orders by Status 📊")
    print("10. Delete an Order 🗑️")
    print("11. Exit 🚪")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        dish_id = int(input("Enter Dish ID: "))
        dish_name = input("Enter Dish Name: ")
        price = float(input("Enter Price: "))
        availability = input(Fore.GREEN+"Is the dish available (yes/no): ").lower() == "yes"

        new_dish = {"dish_id": dish_id, "dish_name": dish_name, "price": price, "availability": availability}
        menu.append(new_dish)
        save_data_to_json(menu, menu_file)
        print(Fore.GREEN+"Dish added to the menu. Bon appétit! 🍽️")
        print(Fore.RESET)

    elif choice == "2":
        dish_id = int(input("Enter Dish ID to remove: "))

        menu = [dish for dish in menu if dish.get("dish_id") != dish_id]
        save_data_to_json(menu, menu_file)
        print(Fore.GREEN+"Dish removed from the menu. Farewell, old friend! 🍽️")
        print(Fore.RESET)

    elif choice == "3":
        snack_id = int(input("Enter Snack ID: "))
        
        snack_name = input("Enter Snack Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        new_snack = {"snack_id": snack_id, "snack_name": snack_name, "price": price, "quantity": quantity}
        snacks.append(new_snack)
        save_data_to_json(snacks, snacks_file)
        print(Fore.GREEN+"Snack added. Snack time! 🍿")
        print(Fore.RESET)

    elif choice == "4":
        take_new_order()

    elif choice == "5":
        try:
            order_id = int(input("Enter Order ID to update status: "))
            if not any(order.get("order_id") == order_id for order in orders):
                print(Fore.RED+"Order not found. Please enter a valid Order ID.")
                print(Fore.RESET)
            else:
                new_status = input("Enter New Status (received/preparing/ready for pickup/delivered): ")
                if new_status not in order_statuses:
                    print(Fore.RED+"Invalid order status. Please enter a valid status.")
                    print(Fore.RESET)
                else:
                    update_order_status(order_id, new_status)
                    print(Fore.GREEN+"Order status updated. The food is on its way! 🚚")
                    print(Fore.RESET)
        except ValueError:
            print("Invalid input. Please enter a valid Order ID.")

    elif choice == "6":
        display_menu()
    
    elif choice == "7":
        display_snacks()

    elif choice == "8":
        display_orders()
    elif choice == "9":
        filter_orders_by_status()
    elif choice == "10":
        order_id_to_delete = int(input("Enter Order ID to delete: "))
        if any(order['order_id'] == order_id_to_delete for order in orders):
            delete_order(order_id_to_delete)
            print(Fore.GREEN+"Order deleted successfully. Say goodbye to that order! 🗑️")
            print(Fore.RESET)
        else:
            print(Fore.RED+"Order not found. Please enter a valid Order ID.")
            print(Fore.RESET)

    elif choice == "11":
        print(Fore.GREEN+"Exiting Zomato Chronicles. Have a great day! 👋")
        print(Fore.RESET)
        break

    else:
        print(Fore.RED+"Invalid choice. Please try again.")
        print(Fore.RESET)
