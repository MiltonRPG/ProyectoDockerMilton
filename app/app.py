from flask import Flask, request, jsonify
from models import db, Item  # Importamos la base de datos y el modelo Item
from dotenv import load_dotenv
import logging
import os

# Cargar las variables de entorno desde .env
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración usando variables de entorno
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la configuración de Flask
db.init_app(app)

# Configuración de logging
log_file = 'logs/log.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s')

# Crear el directorio de logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# Endpoint para crear un nuevo item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    app.logger.info(f"Item created: {new_item.name}")
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

# Endpoint para obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    result = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(result)

# Endpoint para obtener un item por su ID
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({'id': item.id, 'name': item.name})

@app.route('/')
def index():
    return "Hello, Flask!"


# Inicializar la base de datos al inicio de la aplicación
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


