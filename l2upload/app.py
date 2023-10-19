# # app.py
# Import necessary libraries
import json
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash, session
import secrets
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
def generate_secret_key(length=24):
    return secrets.token_hex(length)

secret_key = generate_secret_key()
print(secret_key)



# Helper function to hash passwords
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to save user data to JSON file
def save_user_data(username, password):
    hashed_password = hash_password(password)
    try:
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
        
        data['users'].append({
            'username': username,
            'password': hashed_password
        })
        
        with open('users.json', 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"An error occurred while saving user data: {str(e)}")

# Function to retrieve user data from JSON file
def get_user_data(username):
    try:
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
        
        for user in data['users']:
            if user['username'] == username:
                return user
    except Exception as e:
        print(f"An error occurred while retrieving user data: {str(e)}")
    return None

# Routes

@app.route('/')
def index():
    return 'Welcome to the Flask App!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username is already taken
        existing_user = get_user_data(username)
        if existing_user:
            flash('Username already exists. Please choose a different one.')
        else:
            save_user_data(username, password)
            flash('Registration successful!')
            return redirect(url_for('login'))  # Redirect to login page after registration
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_data(username)
        
        if user:
            stored_password = user['password']
            hashed_password = hash_password(password)
            
            if stored_password == hashed_password:
                session['user_id'] = username
                flash('Login successful!')
                return redirect(url_for('profile'))  # Redirect to profile page after successful login
        
        flash('Login failed. Check your credentials.')
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user_id' in session:
        username = session['user_id']
        user = get_user_data(username)
        
        if user:
            return f'Welcome to your profile, {username}!'
    
    return 'Please log in to access your profile.'

# Configure the file upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload_profile_picture', methods=['POST'])
def upload_profile_picture():
    if 'user_id' in session:
        username = session['user_id']
        file = request.files['profile_picture']
        
        if file:
            # Securely save the uploaded file to the configured folder
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{username}_profile_picture.jpg'))
            
            # You can also store the file path in the database associated with the user
            # to display it on their profile page
            
            flash('Profile picture uploaded successfully')
    
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)


# import json
# import hashlib  # Import the hashlib library
# from flask import Flask,jsonify, request, render_template, redirect, url_for, flash, session
# import os
# from werkzeug.utils import secure_filename
# import secrets

# app = Flask(__name__)
# def generate_secret_key(length=24):
#     return secrets.token_hex(length)

# secret_key = generate_secret_key()
# print(secret_key)



# def save_user_data(username, password):
#     hashed_password = hash_password(password)  # Hash the password
#     try:
#         with open('users.json', 'r') as json_file:
#             data = json.load(json_file)

#         data['users'].append({
#             'username': username,
#             'password': hashed_password  # Save the hashed password
#         })

#         with open('users.json', 'w') as json_file:
#             json.dump(data, json_file)
#     except Exception as e:
#         # Handle the exception (e.g., print an error message)
#         print(f"An error occurred while saving user data: {str(e)}")

    
#     with open('users.json', 'w') as json_file:
#         json.dump(data, json_file)

# def get_user_data(username):
#     with open('users.json', 'r') as json_file:
#         data = json.load(json_file)
    
#     for user in data['users']:
#         if user['username'] == username:
#             return user
    
#     return None

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Check if the username is already taken
#         existing_user = get_user_data(username)
#         if existing_user:
#             flash('Username already exists. Please choose a different one.')
#         else:
#             save_user_data(username, password)
#             flash('Registration successful!')
#             return redirect(url_for('login'))
    
#     return render_template('register.html')



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         user = get_user_data(username)
        
#         if user:
#             stored_password = user['password']
#             hashed_password = hash_password(password)  # Hash the provided password
            
#             if stored_password == hashed_password:
#                 session['user_id'] = username  # Store the username in the session for simplicity
#                 flash('Login successful!')
#                 return redirect(url_for('profile'))
        
#         flash('Login failed. Check your credentials.')
    
#     return render_template('login.html')


# # tests/test_app.py

# # app.py

# # ... (previous code)

# from flask import send_file

# @app.route('/profile')
# def profile():
#     if 'user_id' in session:
#         username = session['user_id']
        
#         # You can retrieve the user's profile picture path from the database
#         # or use the helper function from the previous exercise
#         profile_picture_path = get_user_picture_path(username)
        
#         return f'Welcome to your profile, {username}!<br>' \
#                f'<img id="profile-picture" src="{url_for("profile_picture", username=username)}" alt="Profile Picture">'
    
#     return 'Please log in to access your profile.'

# @app.route('/profile_picture/<username>')
# def profile_picture(username):
#     profile_picture_path = get_user_picture_path(username)
    
#     # Serve the profile picture to the client
#     return send_file(profile_picture_path, as_attachment=False)


# # Configure the file upload folder
# app.config['UPLOAD_FOLDER'] = 'uploads'

# # Helper function to get the user's uploaded picture file path
# def get_user_picture_path(username):
#     return os.path.join(app.config['UPLOAD_FOLDER'], f'{username}_profile_picture.jpg')

# @app.route('/upload_profile_picture', methods=['POST'])
# def upload_profile_picture():
#     if 'user_id' in session:
#         username = session['user_id']
#         file = request.files['profile_picture']
        
#         if file:
#             # Securely save the uploaded file to the configured folder
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{username}_profile_picture.jpg'))
            
#             # You can also store the file path in the database associated with the user
#             # to display it on their profile page
            
#             return 'Profile picture uploaded successfully'
    
#     return 'Please log in to upload a profile picture.'

# # app.py

# # ... (previous code)



# # Initialize a sample list to store resources
# resources = []

# @app.route('/api/resource', methods=['POST'])
# def create_resource():
#     if 'user_id' in session:
#         # Extract data from the JSON request
#         data = request.get_json()
        
#         # Assuming each resource has a 'name' and 'description'
#         name = data.get('name')
#         description = data.get('description')
        
#         # Create a new resource dictionary
#         new_resource = {
#             'id': len(resources) + 1,  # Assign a unique ID (you may use a better mechanism)
#             'name': name,
#             'description': description
#         }
        
#         resources.append(new_resource)
        
#         # Return a success response with the newly created resource and a 201 status code
#         return jsonify(new_resource), 201
    
#     return 'Please log in to create a resource.'


# # app.py

# # ... (previous code)



# # ... (previous code)

# @app.route('/api/resource/<int:resource_id>', methods=['GET'])
# def read_resource(resource_id):
#     # Find the resource by its ID
#     resource = next((res for res in resources if res['id'] == resource_id), None)
    
#     if resource:
#         return jsonify(resource), 200  # Return the resource data as JSON with a 200 status code
    
#     return 'Resource not found', 404

# # app.py

# @app.route('/api/resource/<int:resource_id>', methods=['PUT'])
# def update_resource(resource_id):
#     # Find the resource by its ID
#     resource = next((res for res in resources if res['id'] == resource_id), None)
    
#     if resource:
#         # Extract data from the JSON request
#         data = request.get_json()
        
#         # Update the resource data
#         resource['name'] = data.get('name')
#         resource['description'] = data.get('description')
        
#         return jsonify(resource), 200  # Return the updated resource data as JSON with a 200 status code
    
#     return 'Resource not found', 404

# # app.py

# # ... (previous code)

# # ... (previous code)

# @app.route('/api/resource/<int:resource_id>', methods=['DELETE'])
# def delete_resource(resource_id):
#     global resources  # Declare resources as a global variable
    
#     # Find the resource by its ID
#     resource = next((res for res in resources if res['id'] == resource_id), None)
    
#     if resource:
#         # Remove the resource from the list
#         resources = [res for res in resources if res['id'] != resource_id]
        
#         return '', 204  # Return an empty response with a 204 status code to indicate successful deletion
    
#     return 'Resource not found', 404


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()
