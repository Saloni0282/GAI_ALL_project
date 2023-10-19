# Import Flask app and testing libraries
from app import app
import pytest

# Create a test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the root route
def test_root_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Zesty Zomato!' in response.data

def test_get_menu(client):
    response=client.get("/menu")
    assert response.status_code == 200
    menu=json.loads(response.data)
    assert len(menu) ==3

def test_get_dish(client):
    response=client.get("/menu/1")
    assert response.status_code == 200
    dish=json.loads(response.data)
    assert dish["name"] =="Spaghetti"

def test_add_dish(client):
    dish_data={"dish_id":4,"name":"Rice","price":123.00,"available":False}
    response=client.post("/menu",json=dish_data)
    assert response.status_code == 201
    assert json.loads(response.data)=={"message":"Dish added successfully"}

def test_update_dish(client):
    dish_data={"name":"Pizza","price":401.00,"available":False}
    dish_id_update=2
    response=client.put(f"/menu/{dish_id_update}",json=update_data)
    assert response.status_code == 201
    assert json.loads(response.data)=={"message":"Dish updated successfully"}


# Test deleting a dish from the menu with a valid dish ID
def test_delete_dish_with_valid_dish_id():
    # Add a dish to the menu for testing
    menu.append({"dish_id": 1, "name": "Spaghetti", "price": 12.99, "available": True})
    
    with app.test_client() as client:
        # Send a DELETE request to delete a dish with a valid dish ID
        response = client.delete('/menu/1')
        
        # Check if the response status code is 200 (OK)
        assert response.status_code == 200
        
        # Check if the response data or message indicates that the dish was deleted successfully
        assert b'Dish deleted successfully' in response.data
        
        # Check if the dish is no longer in the menu
        assert not any(dish["dish_id"] == 1 for dish in menu)

# Test deleting a dish from the menu with an invalid dish ID
def test_delete_dish_with_invalid_dish_id():
    with app.test_client() as client:
        # Send a DELETE request to delete a dish with an invalid dish ID
        response = client.delete('/menu/100')  # Dish with ID 100 doesn't exist
        
        # Check if the response status code indicates a not found error (e.g., 404)
        assert response.status_code == 404
        
        # Check if the response data or message indicates that the dish was not found
        assert b'Dish not found' in response.data





# Test taking a new order with valid items
def test_take_order_with_valid_items():
    with app.test_client() as client:
        # Send a POST request to take a new order with valid items
        response = client.post('/take_order', json={
            "customer_name": "Alice",
            "items": [
                {"dish_id": 1, "quantity": 2},
                {"dish_id": 2, "quantity": 1}
            ]
        })
        
        # Check if the response status code is 200 (OK)
        assert response.status_code == 200
        
        # Check if the response data or message indicates a successful order
        assert b'Order taken successfully' in response.data

# Test taking a new order with invalid items
def test_take_order_with_invalid_items():
    with app.test_client() as client:
        # Send a POST request to take a new order with invalid items
        response = client.post('/take_order', json={
            "customer_name": "Bob",
            "items": [
                {"dish_id": 100, "quantity": 2},  # Dish with ID 100 doesn't exist
                {"dish_id": 1, "quantity": 3}
            ]
        })
        
        # Check if the response status code indicates a bad request (e.g., 400)
        assert response.status_code == 400
        
        # Check if the response data or message indicates that the order contains invalid items
        assert b'No valid order items available' in response.data

# Test taking a new order with missing items
def test_take_order_with_missing_items():
    with app.test_client() as client:
        # Send a POST request to take a new order with missing items
        response = client.post('/take_order', json={"customer_name": "Charlie"})
        
        # Check if the response status code indicates a bad request (e.g., 400)
        assert response.status_code == 400
        
        # Check if the response data or message indicates that no order items were provided
        assert b'No order items provided' in response.data



# Import your Flask app and any necessary libraries
from app import app, orders

# Test updating the status of an existing order with a valid status
def test_update_existing_order_status():
    # Add a test order to the orders list
    orders.append({
        "order_id": 1,
        "customer_name": "Alice",
        "items": [{"dish_id": 1, "quantity": 2}],
        "status": "received",
        "total_price": 25.98
    })
    
    with app.test_client() as client:
        # Send a PUT request to update the status of the order
        response = client.put('/order/1', json={"status": "preparing"})
        
        # Check if the response status code is 200 (OK)
        assert response.status_code == 200
        
        # Check if the response data or message indicates a successful status update
        assert b'Order status updated successfully' in response.data
        
        # Check if the order's status is updated in the orders list
        assert orders[0]['status'] == "preparing"

# Test updating the status of a non-existent order
def test_update_nonexistent_order_status():
    with app.test_client() as client:
        # Send a PUT request to update the status of a non-existent order
        response = client.put('/update_order_status/100', json={"status": "ready for pickup"})
        
        # Check if the response status code indicates a not found error (e.g., 404)
        assert response.status_code == 404
        
        # Check if the response data or message indicates that the order was not found
        assert b'Order not found' in response.data

# Test updating the status of an order with an invalid status
def test_update_order_with_invalid_status():
    # Add a test order to the orders list
    orders.append({
        "order_id": 2,
        "customer_name": "Bob",
        "items": [{"dish_id": 2, "quantity": 1}],
        "status": "received",
        "total_price": 12.99
    })
    
    with app.test_client() as client:
        # Send a PUT request to update the status of the order with an invalid status
        response = client.put('/order/2', json={"status": "invalid_status"})
        
        # Check if the response status code indicates a bad request (e.g., 400)
        assert response.status_code == 400
        
        # Check if the response data or message indicates that the status is invalid
        assert b'Invalid status' in response.data
