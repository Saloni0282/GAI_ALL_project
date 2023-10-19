# Import Flask
from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)




# Define a menu as a list of dishes (for simplicity)
menu = [
    {"dish_id":1,"name": "Spaghetti", "price": 12.99, "available": True},
    {"dish_id":2,"name": "Pizza", "price": 400.00, "available": True},
    {"dish_id":3,"name": "Succi", "price":260, "available": False},

    # Add more dishes as needed
]
# Define a list to store orders
orders=[]
order_id_counter=1

# @app.route('/')
# def hello_world():
#     return 'Welcome to Zesty Zomato!'

# Route to get the menu
@app.route('/menu',methods=['GET'])
def get_menu():
    return jsonify(menu)

# Route to add a new dish to the menu
@app.route('/add_dish',methods=['POST'])
def add_dish():
    data=request.get_json()
    menu.append(data)
    return jsonify({"message": "Dish added successfully"}),201

# Route to find dish by id to the menu
@app.route('/menu/<int:dish_id>',methods=['GET'])
def get_dish():
    for dish in menu:
        if dish["dish_id"]==dish_id:
            return jsonify(dish)
    return jsonify("Dish not found"),404

# Route to update dish to the menu
@app.route('/menu/<int:dish_id>',methods=['PUT'])
def update_dish():
    data=request.get_json()
    for dish in menu:
        if dish["dish_id"]==dish_id:
            dish.update(data)
            return jsonify("Dish updated successfully")
    return jsonify("Dish not found"),404



# Route to update the status of an order
@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    new_status = data.get('status')
    
    # Find the order by its ID
    for order in orders:
        if order['order_id'] == order_id:
            # Check if the new status is valid (e.g., 'preparing', 'ready for pickup', 'delivered')
            valid_statuses = ['preparing', 'ready for pickup', 'delivered']
            if new_status in valid_statuses:
                order['status'] = new_status
                return jsonify({"message": "Order status updated successfully"})
            else:
                return jsonify({"message": "Invalid status"}), 400
    
    return jsonify({"message": "Order not found"}), 404


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run()
