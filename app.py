# app.py
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger setup
SWAGGER_URL = '/swagger'  # Swagger UI endpoint
API_DOC = '/static/swagger.json'  # API spec file path
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/api/hello', methods=['GET'])
def hello():
    """Return a simple message."""
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
