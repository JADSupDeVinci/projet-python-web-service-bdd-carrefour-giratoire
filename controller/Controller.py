from flask import Flask, jsonify, request
from database.model.SpecialFeature import SpecialFeature
from database.model.Color import Color
from database.model.Environment import Environment
from database.model.Element import Element
from database.model.DragonType import DragonType
from RandomDragon import RandomDragon



app = Flask(__name__)
@app.route('/getAll/Colors', methods=['GET'])
def getAllColors():
    result = Color.get_all_color()
    return jsonify([color.toDict() for color in result])

@app.route('/getAll/SpecialFeatures', methods=['GET'])
def getAllSpecialFeatures():
    result = SpecialFeature.get_all_special_features()
    return jsonify([special_feature.toDict() for special_feature in result])

@app.route('/getAll/Environments', methods=['GET'])
def getAllEnvironments():
    result = Environment.get_all_environments()
    return jsonify([environment.toDict() for environment in result])

@app.route('/getAll/Elements', methods=['GET'])
def getAllElements():
    result = Element.get_all_elements()
    return jsonify([element.toDict() for element in result])

@app.route('/getAll/DragonTypes', methods=['GET'])
def getAllDragonTypes():
    result = DragonType.get_all_dragon_types()
    return jsonify([dragon_type.toDict() for dragon_type in result])

@app.route('/add/Color', methods=['POST'])
def addColor():
    color_name = request.json['color_name']
    colors = Color.get_all_color()
    for color in colors:
        if color.color_name == color_name:
            return jsonify({'message': 'Color already exists'})

    color = Color(color_name=color_name)
    Color.addColor(color)
    return jsonify({'message': 'Color added successfully'})

@app.route('/delete/Color', methods=['DELETE'])
def deleteColor():
    color_id = request.json['color_id']
    color_id = int(color_id)
    colors = Color.get_all_color()
    for color in colors:
        if color.id == color_id:
            Color.deleteColor(color)
            return jsonify({'message': 'Color deleted successfully'})
    return jsonify({'message': 'Color not found'})

@app.route('/put/Color', methods=['PUT'])
def putColor():
    color_id = request.json['color_id']
    color_name = request.json['color_name']
    color_id = int(color_id)
    colors = Color.get_all_color()
    for color in colors:
        if color.id == color_id:
            color.putColor(color_id, color_name)
            return jsonify({'message': 'Color updated successfully'})
    return jsonify({'message': 'Color not found'})

@app.route('/get/RandomDragon', methods=['GET'])
def getRandomDragon():
    dragon = RandomDragon()
    return jsonify(dragon.toDict())

app.run(host= 'localhost', port=5000)