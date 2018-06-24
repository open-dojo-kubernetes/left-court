import pika


class PlayNotifier(object):
    def __init__(self,):
        self.host = 'localhost'
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))

    def publish_play(self, play: dict, gameIdentifier: int):
        exchange = "plays-game-{}-exchange".format(gameIdentifier)
        routing_key = 'plays-python-{}'.format(gameIdentifier)
        try:
            self.connection.channel().basic_publish(exchange=exchange,
                                                    routing_key=routing_key,
                                                    body=play)
        except ConnectionError:
            print("DAMN YOU WABBIT!")
        print("[x] Sent Score to Queue")
