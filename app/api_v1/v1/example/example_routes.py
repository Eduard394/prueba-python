# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)


@api.route('/lista', methods=['GET'])
def get_lista():
    name = request.args.get('name')
    response = Controller.get_lista(name=name)
    return jsonify(data=response)

@api.route('/lista', methods=['POST'])
def post_save():
    name = request.args.post('name')
    identification = request.args.post('identification')
    response = Controller.save_model(name=name,identification=identification)
    return jsonify(data=response)

