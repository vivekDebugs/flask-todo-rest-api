from flask import Blueprint, request, jsonify

todo_bp = Blueprint('todo', __name__, url_prefix='/todos')

todos = ['todo1', 'todo2', 'todo3']

# Get all todos
@todo_bp.route('/', methods=['GET'])
def get_todos():
    sort = request.args.get('sort')
    response_todos = todos
    if sort == 'asc':
        response_todos = sorted(todos)
    elif sort == 'desc':
        response_todos = sorted(todos, reverse=True)
    return jsonify(response_todos), 200

# Get todo
@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    return jsonify(todos[todo_id]), 200

# Add todo
@todo_bp.route('/', methods=['POST'])
def add_todo():
    todo = request.json['todo']
    todos.append(todo)
    return jsonify(todo), 201

# Update todo
@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = request.json['todo']
    todos[todo_id] = todo
    return jsonify(todo), 200

# Delete todo
@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deleted_todo = todos.pop(todo_id)
    return jsonify(deleted_todo), 200