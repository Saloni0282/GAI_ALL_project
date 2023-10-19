from flask import Flask, jsonify
from app.todo import Todo

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Todo API!"

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'task': todo.task} for todo in todos]
    return jsonify(todo_list)

if __name__ == '__main__':
    app.run()
