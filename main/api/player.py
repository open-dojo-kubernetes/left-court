from typing import Tuple

from flask import request, jsonify
from flask_restful import Resource, fields, reqparse
from injector import inject, Injector

from main.service.play.play_handler import PlayHandler

play_fields = {
    'incomingSide': fields.String,
    'effect': fields.Boolean,
    'innerSide': fields.String,
    'count': fields.Integer,
    'speed': fields.String,
    'height': fields.String
}


class Player(Resource):
    @inject
    def __init__(self):
        self.play_handler = Injector().get(PlayHandler)
        self.parser = reqparse.RequestParser()

    def post(self) -> Tuple[dict, int]:
        """
        This will call the play_handler
        """
        print(request.json)
        if request.json['incomingSide'] == 'RIGHT':
             return self.play_handler.receive_play(request.json), 200
        else:
            return jsonify({"error": "The incoming side should be the right.", "errorCode": 100001}), 501


class Serve(Resource):
    @inject
    def __init__(self):
        self.play_handler = Injector().get(PlayHandler)
        self.parser = reqparse.RequestParser()

    @inject
    def post(self) -> Tuple[dict, int]:
        return self.play_handler.start_service(), 200

