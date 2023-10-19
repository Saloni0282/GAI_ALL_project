import json

inventory_file = "inventory.json"
sales_file = "sales.json"

# Load initial inventory data from the file if it exists
try:
    with open(inventory_file, "r") as file:
        inventory = json.load(file)
except FileNotFoundError:
    inventory = {}

# Load initial sales data from the file if it exists
try:
    with open(sales_file, "r") as file:
        sales_record = json.load(file)
except FileNotFoundError:
    sales_record = {}

def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file)

def save_sales_record(sales_record):
    with open(sales_file, "w") as file:
        json.dump(sales_record, file)

# ... (rest of the code remains the same)


def add_snack(inventory, snack_id, snack_name, snack_price, snack_quantity):
    # Add the snack information to the inventory dictionary
    inventory[snack_id] = {
        'name': snack_name,
        'price': snack_price,
        'quantity': snack_quantity
    }

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for snack_id, snack_info in inventory.items():
            print(f"Snack ID: {snack_id}")
            print(f"Name: {snack_info['name']}")
            print(f"Price: {snack_info['price']}")
            if snack_info['quantity'] > 0:
                print(f"Availability: Available ({snack_info['quantity']} units)")
            else:
                print("Availability: Unavailable")
            print("---------------------------")

def remove_snack(inventory, snack_id):
    if snack_id in inventory:
        del inventory[snack_id]
        print(f"Snack with ID {snack_id} has been removed.")
    else:
        print(f"Snack with ID {snack_id} does not exist in the inventory.")

def update_snack_availability(inventory, snack_id, new_availability):
    if snack_id in inventory:
        if new_availability == 'yes':
            new_quantity = int(input(f"Enter the quantity for Snack with ID {snack_id}: "))
            inventory[snack_id]['quantity'] = new_quantity
            print(f"Snack with ID {snack_id} availability updated to {new_availability} with a quantity of {new_quantity}.")
        else:
            inventory[snack_id]['quantity'] = 0
            print(f"Snack with ID {snack_id} availability updated to {new_availability}.")
    else:
        print(f"Snack with ID {snack_id} does not exist in the inventory.")



def update_snack_sales(inventory, sales_record, snack_id, quantity_sold):
    if snack_id in inventory:
        if inventory[snack_id]['quantity'] >= quantity_sold:
            if snack_id in sales_record:
                sales_record[snack_id] += quantity_sold
            else:
                sales_record[snack_id] = quantity_sold
            inventory[snack_id]['quantity'] -= quantity_sold
            print(f"{quantity_sold} units of Snack with ID {snack_id} sold.")
            if inventory[snack_id]['quantity'] == 0:
                print(f"Snack with ID {snack_id} is now unavailable.")
        else:
            print(f"Insufficient quantity of Snack with ID {snack_id}. Available: {inventory[snack_id]['quantity']} units")
    else:
        print(f"Snack with ID {snack_id} does not exist in the inventory.")

# Function to view the sales record
def view_sales_record():
    if not sales_record:
        print("Sales record is empty.")
    else:
        print("Sales Record:")
        for snack_id, quantity_sold in sales_record.items():
            print(f"Snack ID: {snack_id}, Quantity Sold: {quantity_sold}")

# Main menu
while True:
    print("Menu:")
    print("1. Add Snack")
    print("2. Display Inventory")
    print("3. Remove Snack")
    print("4. Update Snack Availability")
    print("5. Record Snack Sales")
    print("6. View Sales Record")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        snack_id = input("Enter Snack ID: ")
        snack_name = input("Enter Snack Name: ")
        snack_price = float(input("Enter Snack Price: "))
        snack_quantity = int(input("Enter quantity available: "))
        add_snack(inventory, snack_id, snack_name, snack_price, snack_quantity)
        save_inventory(inventory)
    elif choice == '2':
        display_inventory(inventory)
    elif choice == '3':
        snack_id = input("Enter Snack ID to remove: ")
        remove_snack(inventory, snack_id)
        save_inventory(inventory)
    elif choice == '4':
        snack_id = input("Enter Snack ID to update availability: ")
        new_availability = input("Enter new availability ('yes' or 'no'): ")
        update_snack_availability(inventory, snack_id, new_availability)
        save_inventory(inventory)
    elif choice == '5':
        snack_id = input("Enter Snack ID to record sales: ")
        quantity_sold = int(input("Enter quantity sold: "))
        update_snack_sales(inventory, sales_record, snack_id, quantity_sold)
        save_inventory(inventory)
        save_sales_record(sales_record)
    elif choice == '6':
        view_sales_record()
    elif choice == '7':
        print("Thank you for visiting Mumbai Munchines!!!!")
        break
    else:
        print("Invalid choice. Please try again.")

# Make sure to save the final state of inventory and sales record before exiting
save_inventory(inventory)
save_sales_record(sales_record)
