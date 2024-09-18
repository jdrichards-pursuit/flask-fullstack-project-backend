from flask import Blueprint, request, jsonify
import pandas as pd

# use this path to import data by adding the csv file name to the end of the path
# data_path = 'data/'


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return "Welcome to the Flask Starter"

@api.route('/get', methods=['GET'])
def get_route():
    return 'This method will return all items for your GET'

@api.route('/post', methods=['POST'])
def post_route():
  return 'This method will be used to add an item to the csv or data'

