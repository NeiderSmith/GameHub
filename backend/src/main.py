# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.game import Game, GameSchema
from .entities.user import User, UserSchema
from .entities.score import Score, ScoreSchema
from .entities.gamecategory import GameCategory, GameCategorySchema
from flask_cors import CORS, cross_origin
from datetime import datetime
import os

# Instancia de aplicación Flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# De ser necesario, se genera el esquema de base de datos
Base.metadata.create_all(engine)

# Solucion a problema de CORS
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

# ENDPOINTS 
@app.route('/games', methods=['GET'])
def get_games():
    # Obtener objetos de base de datos
    session = Session()
    game_objects = session.query(Game).all()

    # Transformar en Json
    schema = GameSchema(many=True)
    games = schema.dump(game_objects)

    # Cerrar conexión de base de datos
    session.close()

    return jsonify(games)

@app.route('/games/active', methods=['GET'])
def get_active_games():
    # Obtener objetos de base de datos
    session = Session()
    game_objects = session.query(Game).filter_by(active=True)

    # Transformar en Json
    schema = GameSchema(many=True)
    games = schema.dump(game_objects)

    # Cerrar conexión de base de datos
    session.close()

    return jsonify(games)

@app.route('/games/<id>', methods=['GET'])
def get_game(id):
    # Obtener objetos de base de datos
    session = Session()
    game_object = session.query(Game).get(id)

    # Transformar en Json
    schema = GameSchema(many=False)
    games = schema.dump(game_object)
    print(games)

    # Cerrar conexión de base de datos
    session.close()

    return jsonify(games)


@app.route('/games', methods=['POST'])
def add_game():

    # Obtención de Json de data
    data = request.get_json()

    data['active'] = True if True else False
    # Validación de datos mediante esquema de objeto
    posted_game = GameSchema(only=('title', 'description', 'release_date', 'cover_image', 'category_id', 'active')).load(data)

    # Creación de obtejo con base en esquema validado
    game = Game(**posted_game, created_by="HTTP post request")

    # Persistir la entidad en la base de datos
    session = Session()
    session.add(game)
    session.commit()

    # Devolver el esquema de la entidad agregada a base de datos
    new_game = GameSchema().dump(game)
    session.close()

    return jsonify(new_game), 201

@app.route('/games/<id>', methods=['PUT'])
def update_game(id):
    session = Session()

    # Obtener objeto de base de datos
    game = session.query(Game).get(id)

    # Extraer atributos del Json recibido
    title = request.json['title']
    description = request.json['description']
    release_date = request.json['release_date']
    cover_image = request.json['cover_image']
    category_id = request.json['category_id']
    active = request.json['active']

    # Modificar el objeto entidad traido anteriormente con los datos del Json
    game.title = title
    game.description = description
    game.release_date = release_date
    game.cover_image = cover_image
    game.category_id = category_id
    game.active = active

    session.commit()

    # Devolver el esquema de la entidad actualizada en base de datos
    edited_game = GameSchema().dump(game)

    return jsonify(edited_game), 201

@app.route("/games/<id>", methods=["DELETE"])
def delete_game(id):
    session = Session()

    # Obtener objeto de base de datos
    game = session.query(Game).get(id)

    # Eliminar objeto
    session.delete(game)
    session.commit()

    return jsonify("Eliminado exitosamente"), 201

if __name__ == "__main__":
    app.run(debug=True)