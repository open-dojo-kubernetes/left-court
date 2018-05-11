from flask_restful import Api, Resource

from api.player import Player
from api.player import Serve
from flask import Flask, make_response

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self) -> dict:
        return make_response("READY TO ROCK", 200)


api.add_resource(Health, '/health', endpoint='health')
api.add_resource(Player, '/left/play', endpoint='play')
api.add_resource(Serve, '/left/serve', endpoint='serve')

if __name__ == '__main__':
    app.run(debug=True)
