from flask import Flask, jsonify, request
from routes.auth import auth_blueprint
from routes.admin import admin_blueprint
from routes.user import user_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Or load from .env

# Register Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
