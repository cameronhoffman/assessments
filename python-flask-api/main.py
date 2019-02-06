from flask import Flask, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

from models import ItemList, Item

app = Flask(__name__)

def model_array_to_list(array):
    return list(map(lambda l: model_to_dict(l), array))

@app.route('/')
def healthcheck():
    return 'ok'

@app.route('/lists')
def get_all_lists():
    item_lists = ItemList.select()

    return jsonify(model_array_to_list(item_lists))
