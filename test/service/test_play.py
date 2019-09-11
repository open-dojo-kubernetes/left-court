import requests
from flask import Flask
from flask_restful import Api
from flask_testing import LiveServerTestCase

from main.api.player import Player, Serve
from main.app import Health


class TestFlaskApiUsingRequests(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(Health, '/health', endpoint='health')
        api.add_resource(Player, '/left/play', endpoint='play')
        api.add_resource(Serve, '/left/serve', endpoint='serve')
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_app_health(self):
        response = requests.get(self.get_server_url() + '/health')
        self.assertEqual("Are you inn-sewer-red that this thing is gonna work, make sure that you have lots of pink "
                         "ink.",
                         response.text)

    # def test_play_handler_receive_play_correct(self):
    #    incoming_play = dict(incomingSide='RIGHT', effect=False, innerSide='RIGHT', count=0, speed='AVG', height='LOW')
    #     response_play = requests.post(self.get_server_url()+'/left/play', data=incoming_play).json()
    #     self.assertEqual('LEFT', response_play['incomingSide'])
    #     self.assertTrue(response_play['effect'])
    #     self.assertEqual(1, response_play['count'])
