from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

from models import ItemList, Item

app = Flask(__name__)

def model_array_to_list(array):
    return list(map(lambda l: model_to_dict(l), array))

def make_error_response(message, http_code):
    """Creates a Flask response based on a error

    :param error: the WebError
    """
    return jsonify({"error": message}), http_code, {'Content-Type': 'application/json'}

@app.route('/')
def healthcheck():
    return 'ok'

@app.route('/lists')
def get_all_lists():
    item_lists = ItemList.select()

    return jsonify(model_array_to_list(item_lists))

@app.route('/lists', methods=['POST'])
def create_list():
    body = request.get_json()

    itemlist = ItemList.create(
        name=body['name']
    )

    return jsonify(model_to_dict(itemlist)), 201
