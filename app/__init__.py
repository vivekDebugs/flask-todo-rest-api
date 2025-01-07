from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    # Register blueprint
    from app.controllers.todo_controller import todo_bp
    app.register_blueprint(todo_bp)

    return app