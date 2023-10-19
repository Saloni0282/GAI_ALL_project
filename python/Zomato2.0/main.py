import json
import os
from tabulate import tabulate
from colorama import Fore

# Define file names
menu_file = "menu.json"
snacks_file = "snacks.json"
orders_file = "orders.json"
feedback_file = "feedback.json"  # New feedback file

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
feedback = load_data(feedback_file)  # New feedback data

# Function to update order status
def update_order_status(order_id, new_status):
    for order in orders:
        if order.get("order_id") == order_id:
            order["status"] = new_status
            save_data_to_json(orders, orders_file)
            break

# Function to calculate and display the total price of an order
# Function to calculate and display the total price of an order
def calculate_order_total(order_id):
    for order in orders:
        if order.get("order_id") == order_id:
            total_price = 0
            total_quantity = 0
            customer_name = order.get("customer_name")
            customer_id = order.get("order_id")

            print(f"Customer ID: {customer_id}, Customer Name: {customer_name}")

            # Create a list for tabulate
            table = []

            # Calculate the total price and quantity for dishes
            for dish_id, quantity in order.get("dishes", {}).items():
                for dish in menu:
                    if dish.get("dish_id") == int(dish_id):  # Convert dish_id to int
                        dish_name = dish.get("dish_name")
                        dish_price = dish.get("price", 0)
                        total_price += dish_price * quantity
                        total_quantity += quantity
                        table.append(["Dish", dish_id, dish_name, quantity, f"${dish_price:.2f}"])

            # Calculate the total price and quantity for snacks
            for snack_id, quantity in order.get("snacks", {}).items():
                for snack in snacks:
                    if snack.get("snack_id") == int(snack_id):  # Convert snack_id to int
                        snack_name = snack.get("snack_name")
                        snack_price = snack.get("price", 0)
                        total_price += snack_price * quantity
                        total_quantity += quantity
                        table.append(["Snack", snack_id, snack_name, quantity, f"${snack_price:.2f}"])

            # Display the table with tabulate
            headers = ["Item Type", "Item ID", "Item Name", "Quantity", "Price(Per/piece)"]
            print(Fore.GREEN + tabulate(table, headers, tablefmt="grid"))

            print(Fore.GREEN + f"Total Quantity: {total_quantity}, Total Price: ${total_price:.2f}")
            print(Fore.RESET)
            break
    else:
        print("Order not found.")



# Function to display the menu
def display_menu():
    if not menu:
        print("The menu is empty.")
        return
    # Create a list of lists for tabulate
    table = []
    for dish in menu:
        dish_id = dish['dish_id']
        dish_name = dish['dish_name']
        price = dish['price']
        availability = dish['availability']
        quantity = dish.get('quantity', 0)

        table.append([dish_id, dish_name, f"${price:.2f}", quantity, availability])

    # Define table headers
    headers = ["Dish ID", "Dish Name", "Price", "Quantity", "Availability"]

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
# Function to take a new order
def take_new_order():
    customer_name = input("Enter Customer Name: ")

    print("Do you want to add snacks to the order? (yes/no): ")
    add_snacks = input().strip().lower() == "yes"
    ordered_snacks = {}
    if add_snacks:
        if not snacks:
            print("There are no snacks available to add to the order.")
            return
        print(Fore.GREEN + "Available Snacks:")
        display_snacks()
        while True:
            snack_ids = [int(x) for x in input("Enter Snack IDs (comma-separated): ").split(",")]
            invalid_ids = [snack_id for snack_id in snack_ids if snack_id not in [snack['snack_id'] for snack in snacks]]
            if invalid_ids:
                print(Fore.RED + f"Invalid Snack IDs: {', '.join(map(str, invalid_ids))}. Please enter valid Snack IDs.")
            else:
                break

        for snack_id in snack_ids:
            quantity = int(input(f"Enter quantity for Snack ID {snack_id}: "))
            for snack in snacks:
                if snack['snack_id'] == snack_id:
                    if quantity > snack['quantity']:
                        print(Fore.RED + "Invalid quantity. Quantity exceeds availability.")
                        return
                    snack['quantity'] -= quantity
                    if snack['quantity'] == 0:
                        snack['availability'] = False
                    ordered_snacks[snack_id] = quantity

    print("Do you want to add dishes to the order? (yes/no): ")
    add_dishes = input().strip().lower() == "yes"
    ordered_dishes = {}
    if add_dishes:
        if not menu:
            print("The menu is empty. There are no dishes available to add to the order.")
            return
        print(Fore.GREEN + "Available Dishes:")
        display_menu()
        while True:
            dish_ids = [int(x) for x in input("Enter Dish IDs (comma-separated): ").split(",")]
            invalid_ids = [dish_id for dish_id in dish_ids if dish_id not in [dish['dish_id'] for dish in menu]]
            if invalid_ids:
                print(Fore.RED + f"Invalid Dish IDs: {', '.join(map(str, invalid_ids))}. Please enter valid Dish IDs.")
            else:
                break

        for dish_id in dish_ids:
            quantity = int(input(f"Enter quantity for Dish ID {dish_id}: "))
            for dish in menu:
                if dish['dish_id'] == dish_id:
                    if quantity > dish['quantity']:
                        print(Fore.RED + "Invalid quantity. Quantity exceeds availability.")
                        return
                    dish['quantity'] -= quantity
                    if dish['quantity'] == 0:
                        dish['availability'] = False
                    ordered_dishes[dish_id] = quantity

    if not ordered_snacks and not ordered_dishes:
        print("You must select at least one snack or dish to place an order.")
        return

    new_order_id = max([order.get("order_id", 0) for order in orders], default=0) + 1
    order_status = "received"
    new_order = {"order_id": new_order_id, "customer_name": customer_name, "snacks": ordered_snacks,
                 "dishes": ordered_dishes, "status": order_status}
    orders.append(new_order)
    save_data_to_json(orders, orders_file)
    print(Fore.GREEN + "Order taken successfully. Enjoy your meal! 🍔")
    print(Fore.RESET)


# Function to display orders

def display_orders():
    if not orders:
        print("There are no customer orders.")
        return

    print("\nCustomer Orders:")
    table = []
    for order in orders:
        order_id = order.get("order_id")
        customer_name = order.get("customer_name")
        order_status = order.get("status")

        # Get the list of snack and dish IDs ordered by the customer
        snack_ids_ordered = order.get("snacks", {}).keys()
        dish_ids_ordered = order.get("dishes", {}).keys()

        # Use list comprehensions to get the names of snacks and dishes
        snacks_ordered = [snack["snack_name"] for snack in snacks if str(snack["snack_id"]) in snack_ids_ordered]
        dishes_ordered = [dish["dish_name"] for dish in menu if str(dish["dish_id"]) in dish_ids_ordered]

        # Create comma-separated strings for snacks and dishes
        snacks_str = ", ".join(snacks_ordered)
        dishes_str = ", ".join(dishes_ordered)

        table.append([order_id, customer_name, snacks_str, dishes_str, order_status])

    headers = ["Order ID", "Customer Name", "Snacks", "Dishes", "Status"]

    if not table:
        print("No customer orders found.")
    else:
        print(Fore.GREEN + tabulate(table, headers, tablefmt="grid"))
        print(Fore.RESET)




# Modify the filter_orders_by_status function
def filter_orders_by_status(filter_status):
    filtered_orders = [order for order in orders if order.get("status") == filter_status]
    if not filtered_orders:
        print(f"No orders with status '{filter_status}' found.")
    else:
        print(f"Orders with status '{filter_status}':")
        table = []
        for order in filtered_orders:
            order_id = order.get("order_id")
            customer_name = order.get("customer_name")
            table.append([order_id, customer_name, filter_status])

        headers = ["Order ID", "Customer Name", "Status"]

        # Print the formatted table with colored text
        print(Fore.CYAN + tabulate(table, headers, tablefmt="grid"))
        print(Fore.RESET)

# Function to collect feedback for an order
def collect_feedback(order_id, rating, comment):
    for order in orders:
        if order.get("order_id") == order_id:
            if "feedback" not in order:
                order["feedback"] = []
            order["feedback"].append({"rating": rating, "comment": comment})
            save_data_to_json(orders, orders_file)
            
            # Add feedback to the feedback data
            feedback.append({"order_id": order_id, "rating": rating, "comment": comment})
            save_data_to_json(feedback, feedback_file)  # Save feedback data
            print(Fore.GREEN + "Feedback collected successfully. Thank you for your feedback!")
            print(Fore.RESET)
            break
    else:
        print(Fore.RED + "Order not found.")
        print(Fore.RESET)

# Function to display feedback
def display_feedback():
    if not feedback:
        print("There is no feedback available.")
        return
    
    # Create a list of lists for tabulate
    table = []
    for fb in feedback:
        order_id = fb.get("order_id")
        rating = fb.get("rating")
        comment = fb.get("comment")
        table.append([order_id, rating, comment])

    # Define table headers
    headers = ["Order ID", "Rating", "Comment"]

    # Print the formatted table with colored text
    print(Fore.CYAN + tabulate(table, headers, tablefmt="grid"))
    print(Fore.RESET)

# Function to apply a discount to a dish
def apply_discount_to_dish(dish_id, discount_percentage):
    for dish in menu:
        if dish.get("dish_id") == dish_id:
            original_price = dish.get("price")
            discounted_price = original_price - (original_price * discount_percentage / 100)
            dish["price"] = discounted_price
            save_data_to_json(menu, menu_file)
            print(f"Discount of {discount_percentage}% applied to {dish.get('dish_name')}. New price: ${discounted_price:.2f}")
            break
    else:
        print("Dish not found.")

# Function to apply a discount to an order
def apply_discount_to_order(order_id, discount_percentage):
    for order in orders:
        if order.get("order_id") == order_id:
            total_price = 0
            for dish_id in order.get("dishes", []):
                for dish in menu:
                    if dish.get("dish_id") == dish_id:
                        total_price += dish.get("price", 0)
            original_price = total_price
            discounted_price = original_price - (original_price * discount_percentage / 100)
            order["total_price"] = discounted_price
            save_data_to_json(orders, orders_file)
            print(f"Discount of {discount_percentage}% applied to Order #{order_id}. New total price: ${discounted_price:.2f}")
            break
    else:
        print("Order not found.")


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
    print("10. Calculate Order Total 💰")
    print("11. Collect Customer Feedback 📝")
    print("12. Apply Discount to Dish 🍽️")
    print("13. Apply Discount to Order 📉")
    print("14. Show Feedback 🌟")  # New option to show feedback
    
    print("15. Exit 🚪")
    print("16. Delete an Order 🗑️")

    choice = input("Enter your choice: ")

    if choice == "1":
    
        dish_id = int(input("Enter Dish ID: "))
        dish_name = input("Enter Dish Name: ")
        price = float(input("Enter Price: "))
        availability = input(Fore.GREEN + "Is the dish available (yes/no): ").lower() == "yes"
        quantity = int(input("Enter Quantity: "))  # Add this line to get quantity

        new_dish = {
            "dish_id": dish_id,
            "dish_name": dish_name,
            "price": price,
            "availability": availability,
            "quantity": quantity,  # Store the quantity in the menu
        }
        menu.append(new_dish)
        save_data_to_json(menu, menu_file)
        print(Fore.GREEN + "Dish added to the menu. Bon appétit! 🍽️")
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
        filter_status = input("Enter Order Status to filter (received/preparing/ready for pickup/delivered): ").strip().lower()
        filter_orders_by_status(filter_status)

    elif choice == "10":
        order_id = int(input("Enter Order ID to Calculate Total: "))
        calculate_order_total(order_id)

    elif choice == "11":
        order_id = int(input("Enter Order ID to Collect Feedback: "))
        rating = int(input("Enter Rating (1-5): "))
        comment = input("Enter Comment: ")
        collect_feedback(order_id, rating, comment)

    elif choice == "12":
        dish_id = int(input("Enter Dish ID to Apply Discount: "))
        discount_percentage = float(input("Enter Discount Percentage (0-100): "))
        apply_discount_to_dish(dish_id, discount_percentage)

    elif choice == "13":
        order_id = int(input("Enter Order ID to Apply Discount: "))
        discount_percentage = float(input("Enter Discount Percentage (0-100): "))
        apply_discount_to_order(order_id, discount_percentage)

    elif choice == "14":
        display_feedback()  # Show feedback

    elif choice == "15":
        print(Fore.GREEN + "Exiting Zomato Chronicles. Have a great day! 👋")
        print(Fore.RESET)
        break
    elif choice == "16":
        order_id_to_delete = int(input("Enter Order ID to delete: "))
        if any(order['order_id'] == order_id_to_delete for order in orders):
            delete_order(order_id_to_delete)
            print(Fore.GREEN+"Order deleted successfully. Say goodbye to that order! 🗑️")
            print(Fore.RESET)
        else:
            print(Fore.RED+"Order not found. Please enter a valid Order ID.")
            print(Fore.RESET)
    else:
        print(Fore.RED+"Invalid choice. Please try again.")
        print(Fore.RESET)
