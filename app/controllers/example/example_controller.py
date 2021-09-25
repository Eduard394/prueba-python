# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel
from flask import jsonify
from app import db


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_lista(name=None):
        try:

            filtros_kwargs = [
            ]
            if name:
                auxfilter = { 'field': 'name', 'op': '==', 'value': name }
                filtros_kwargs.append(auxfilter)

            examples = ExampleModel.query.filter(*filtros_kwargs)
            final = []
            for user in examples:
                auxiliar = {
                'id': user.id,
                'name': user.name,
                'identification': user.identification
                }
                final.append(auxiliar)
            response = {
                'ok': True,
                'resultado': final
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def save_model(name,identification):
        try:
            usuario = ExampleModel(
            name,
            identification,
            'usuario prueba'
            )
            usuario.save()
            response = {
                'ok': True,
                'message': 'Usuario Guardado exitosamente'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
