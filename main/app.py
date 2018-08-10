from flask import Flask, make_response
from flask_restful import Api, Resource

from main.api.player import Player
from main.api.player import Serve

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self) -> dict:
        return make_response(
            "Are you inn-sewer-red that this thing is gonna work, make sure that you have lots of pink ink.", 200)


api.add_resource(Health, '/health', endpoint='health')
api.add_resource(Player, '/left/play', endpoint='play')
api.add_resource(Serve, '/left/serve', endpoint='serve')

if __name__ == '__main__':
    app.run(debug=True)
